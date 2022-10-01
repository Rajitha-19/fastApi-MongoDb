from mongoengine import Document,StringField,IntField,ListField
class employee(Document):
    name=StringField(max_length=100)
    age=IntField()
    teams=ListField()
