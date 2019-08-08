## DataBase1

* SQLite
```
import sqlite3

conn = sqlite3.connect('test.db')

curs = conn.cursor()
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("has3ong")'
)

conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())
conn.close()
```

* MySQL
```
import mysql

conn = mysql.connector.connect('127.0.0.1')

cursor = conn.cursor()

cursor.execute(
    'CREATE DATABASE test'
)

cursor.execute('CREATE TABLE persons('
               'id int NOT NULL AUTO_INCREMENT,'
               'name varchar(100) NOT NULL',
               'PRIMARY KEY(id))')

cursor.execute('INSERT INTO persons(name) values("has3ong")')
cursor.commit()
cursor.execute('SELECT * FROM persons')

for row in cursor:
    print(row)

cursor.close()
conn.close()
```

* SQLAlchemy
```
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///:memory:')
Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person = Person(name='has3ong')
session.add(person)
session.commit()

ret = session.query(Person).all()
for i in ret:
    print(i.id, i.name)
```
```
1 has3ong
```
* MongoDB
```
import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['test']

stack1 = {
    'name': 'customer1',
    'pip': ['pyhon', 'java'],
    'info': {'os': 'mac'},
    'data' : datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
print(db_stacks.find_one({'_id': stack_id}))
```
```
5d4bd1589cadae04f23ccc5a <class 'bson.objectid.ObjectId'>
{'_id': ObjectId('5d4bd1589cadae04f23ccc5a'), 'name': 'customer1', 'pip': ['pyhon', 'java'], 'info': {'os': 'mac'}, 'data': datetime.datetime(2019, 8, 8, 7, 38, 0, 240000)}
```
