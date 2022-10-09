from UserDb import UserDb
from pprint import pprint

if __name__ == '__main__':
    # предварительно нужно создать базу данных
    name_db = 'netology_db'
    login = 'postgres'
    # pwd = ''
    with open('pwd.txt', encoding='utf-8') as f:
        pwd = f.readline()

    clients_list_ = [
        ('Петров', 'Петр', 'pp@mail.ru', '+7(911) 400-40-50'),
        ('Яшина', 'Надежда', 'yashan@ya.ru', None),
        ('Соколов', 'Леонид', 'sokol@gmail.com', '+7(906) 310-00-18'),
        ('Сидоров', 'Павел', 'sid@bk.ru', '+7(901) 421-00-31'),
        ('Сидоров', 'Леонид', 'lsid@list.ru', '+7(951) 451-70-11')
    ]
    # создаём экземпляр класса
    me = UserDb(name_db, login, password=pwd)

    # применяем различные методы
    me.delete_tables()
    me.create_tables()
    me.add_client('Иванов', 'Иван', 'aaa@bk.ru', '+7(900) 451-45-45')
    me.add_clients_list(clients_list_)
    me.add_phone_num(1, '+7(900) 451-45-46')
    me.delete_phone_num(2, '+7(911) 400-40-50')
    pprint(me.get_data(1))
    me.change_client(3, last_name='Соколова')
    me.delete_client(2)
    print(me.find_client(phone_num='+7(900) 451-45-46'))
    print(me.find_client(last_name='Сидоров', first_name='Павел'))
    me.close()
