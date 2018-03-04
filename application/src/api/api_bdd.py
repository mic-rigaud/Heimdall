# @Author: michael
# @Date:   28-Oct-2017
# @Project: Blueberry
# @Filename: api_bdd.py
# @Last modified by:   michael
# @Last modified time: 04-Mar-2018
# @License: GNU GPL v3

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


class Task(BaseModel):
    action = CharField()
    time = DateTimeField(default=datetime.datetime.now)
