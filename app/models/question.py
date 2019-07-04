from mongoengine import *

class QuestionModel(Document):
    id = StringField(primary_key=True)
    question = StringField()