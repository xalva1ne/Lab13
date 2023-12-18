#Django

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

#SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

class User(SQLAlchemy.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128))
    password = Column(String(128))