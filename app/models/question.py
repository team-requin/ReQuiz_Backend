from mongoengine import *

class QuestionModel(Document):
    gar = StringField(primary_key=True)
    uuid = StringField()
    user = StringField()
    question = ListField(
        n = DictField(
            q = StringField(),
            a = StringField(),
            null=True
    ))