from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import json

with open('pwd.txt', encoding='utf-8') as f:
    password = f.readline()

login = 'postgres'
pwd = password
db_name = 'book_store'

DSN = f'postgresql://{login}:{pwd}@localhost:5432/{db_name}'
engine = sqla.create_engine(DSN)

# Создаём базу данных, если не существует
if not database_exists(engine.url):
    create_database(engine.url)

# Создаём таблицы
create_tables(engine)

with open('tests_data.json', encoding='utf-8') as in_file:
    data = json.load(in_file)

Session = sessionmaker(bind=engine)
session = Session()

# Заполнение таблиц
for row in data:
    model = {'publisher': Publisher, 'shop': Shop, 'book': Book, 'stock': Stock, 'sale': Sale}[row.get('model')]
    session.add(model(id=row.get('pk'), **row.get('fields')))
session.commit()

# session.query(Publisher).filter(Publisher.id == 1).delete()
# session.commit()

# выводим издателя по ID
q = session.query(Publisher).filter(Publisher.id == input('Введите publisher_id: ')).all()
print(*q)

# Название книг и магазины, для которых кол-во книг на складе больше 10
q1 = session.query(Book.title, Shop.name, Stock.count)
q1 = q1.join(Stock, Stock.id_book == Book.id)
q1 = q1.join(Shop, Shop.id == Stock.id_shop).filter(Stock.count > 10).order_by(Stock.count)
print('Запрос 1', *q1.all(), sep='\n')

# Запрос 2
q2 = session.query(Shop.name.distinct(), Sale.price).join(Shop.books1).join(Stock.sales).filter(Sale.price < 50)
print('Запрос 2', *q2.all(), sep='\n')

session.close()
