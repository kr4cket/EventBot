from peewee import *
from bot.core.db.model.BaseModel import BaseModel


class Users(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(null=False)
    photo = BlobField()
    university = CharField(default=0)
    city = IntegerField(default=0)
