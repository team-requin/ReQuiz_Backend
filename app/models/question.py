from mongoengine import *

class QuestionModela(Document):
    id = StringField(primary_key=True)
    question = ListField(
        StringField(),
        null=True
    )
