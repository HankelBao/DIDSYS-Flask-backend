import orm as mongodb

class EmbeddedClassScores(mongodb.EmbeddedDocument):
    date = mongodb.Field()
    subject = mongodb.Field()
    scores = mongodb.Field()

class EmbeddedInspectorClasses(mongodb.EmbeddedDocument):
    name = mongodb.Field()

class EmbeddedInspectorSubjects(mongodb.EmbeddedDocument):
    name = mongodb.Field()

class Record(mongodb.Document):
    className = mongodb.Field()
    subjectName = mongodb.Field()
    inspectorName = mongodb.Field()
    date = mongodb.Field()
    time = mongodb.Field()
    score = mongodb.Field()

class Class(mongodb.Document):
    name = mongodb.Field()
    scores = mongodb.ListField()

class Subject(mongodb.Document):
    name = mongodb.Field()
    
class Inspector(mongodb.Document):
    name = mongodb.Field()
    password = mongodb.Field()
    classes = mongodb.ListField()
    subjects = mongodb.ListField()