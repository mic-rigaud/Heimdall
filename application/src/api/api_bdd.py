from peewee import *
from playhouse.sqlite_ext import SqliteDatabase
import datetime


db = SqliteDatabase('network.db')

class BaseModel(Model):
    class Meta:
        database = db

class Ip(BaseModel):
    ip = CharField()
    mac = CharField()
    time_first = DateTimeField(default=datetime.datetime.now)
    time_last = DateTimeField(default=datetime.datetime.now)
    confiance = BooleanField(default=False)
    status = BooleanField(default=True)

class Parametre(BaseModel):
    section = CharField()
    key = CharField(unique=True)
    value = CharField()



# db.connect()
# db.create_tables([Ip, Parametre])


# class Tweet(BaseModel):
#     user = ForeignKeyField(User, related_name='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)
