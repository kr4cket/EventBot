from peewee import *
from bot.core.db.model.BaseModel import BaseModel
from bot.core.db.model.Users import Users


class Events(BaseModel):
    id = PrimaryKeyField(null=False)
    owner_id = ForeignKeyField(Users, to_field='id')
    name = CharField(null=False)
    photo = BlobField()
    description = TextField()
    university = CharField(default=0)
    city = IntegerField(default=0)
    guests = IntegerField(default=0)
    max_guests = IntegerField(default=20)
