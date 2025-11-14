from django.db import models
from mongoengine import Document, StringField, IntField



# Create your models here.
class Tour(Document):
    name = StringField(required=True)
    location = StringField()
    price = IntField()

