import sqlite3


class Singleton(type):
    __isntance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__isntance:
            cls.__isntance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__isntance[cls]


class Database(metaclass=Singleton):

    connection = None

    def __init__(self):
        self.cursor = None

    def connect(self):
        if self.connection is None:
            print('Não temos ainda uma conexão.. vamos cria-la')
            self.connection = sqlite3.connect('db.geek')
            self.cursor = self.connection.cursor()
        return self.cursor


db1 = Database().connect()

db2 = Database().connect()
