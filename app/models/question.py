from mongoengine import *

class QuestionModel(Document):
    gar = StringField(primary_key=True)

    uuid = StringField()

    user = StringField()

    name = StringField()

    question = DictField(
        n = DictField(
            q = StringField(),
            a = StringField(),
            null=True
    ))