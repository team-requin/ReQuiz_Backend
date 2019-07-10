from mongoengine import *

class UserModel(Document):
    id = StringField(primary_key=True)
    pw = StringField()
    name = StringField()
    level = IntField()
    exp = IntField()