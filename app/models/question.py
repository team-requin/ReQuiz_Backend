from mongoengine import *

class QuestionModel(Document):
    id = StringField(primary_key=True)
    uuid = StringField()
    question = DictField(
        q = StringField(),
        a = StringField(),
        null=True
    )