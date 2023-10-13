from mongoengine import *

connect(host="mongodb+srv://moivvas:password@moivvas.am1rhde.mongodb.net/hw8_1?retryWrites=true&w=majority")

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField(max_length=None)    
    
class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField()
    