import orm as mongodb

class EmbeddedClassWeeklyScore(mongodb.EmbeddedDocument):
    date = mongodb.Field()
    scores = mongodb.Field()

class EmbeddedClassMonthlyScore(mongodb.EmbeddedDocument):
    date = mongodb.Field()
    scores = mongodb.Field()

class EmbeddedInspectorClass(mongodb.EmbeddedDocument):
    name = mongodb.Field()

class EmbeddedInspectorSubject(mongodb.EmbeddedDocument):
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
    weekly_scores = mongodb.ListField()
    monthly_scores = mongodb.ListField()

class Subject(mongodb.Document):
    name = mongodb.Field()
    
class Inspector(mongodb.Document):
    __primary__ = "name"
    name = mongodb.Field()
    password = mongodb.Field()
    classes = mongodb.ListField()
    subjects = mongodb.ListField()