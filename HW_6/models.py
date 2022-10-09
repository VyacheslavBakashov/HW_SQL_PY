import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(30), nullable=False, unique=True)
    books = relationship('Book', backref='publisher')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'
    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String(80), nullable=False)
    id_publisher = sqla.Column(sqla.Integer, sqla.ForeignKey('publisher.id', ondelete='CASCADE'), nullable=False)

    shops = relationship('Stock', back_populates='book1')


class Shop(Base):
    __tablename__ = 'shop'

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(30), nullable=False, unique=True)

    books1 = relationship('Stock', back_populates='shop')


class Stock(Base):
    __tablename__ = 'stock'
    id = sqla.Column(sqla.Integer, primary_key=True)
    id_book = sqla.Column(sqla.Integer, sqla.ForeignKey('book.id',  ondelete='CASCADE'), nullable=False)
    id_shop = sqla.Column(sqla.Integer, sqla.ForeignKey('shop.id', ondelete='CASCADE'), nullable=False)
    count = sqla.Column(sqla.Integer)
    sqla.CheckConstraint('count > 0', name='stock_count_check')

    book1 = relationship(Book, back_populates='shops')
    shop = relationship(Shop, back_populates='books1')


class Sale(Base):
    __tablename__ = 'sale'
    id = sqla.Column(sqla.Integer, primary_key=True)
    price = sqla.Column(sqla.Numeric, nullable=False)
    date_sale = sqla.Column(sqla.Date, nullable=False)
    id_stock = sqla.Column(sqla.Integer, sqla.ForeignKey('stock.id', ondelete='CASCADE'), nullable=False)
    count = sqla.Column(sqla.Integer)
    sqla.CheckConstraint('count > 0', name='sale_count_check')

    stock = relationship(Stock, backref='sales')


def create_tables(engine_):
    Base.metadata.drop_all(engine_)
    Base.metadata.create_all(engine_)
