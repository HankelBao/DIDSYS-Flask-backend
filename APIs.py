from DirectAPIFramework import DirectAPIRegister
from MongoOrm import MongoClient

class RootAPI:
    def __init__(self, DirectAPI:DirectAPIRegister):
        DirectAPI.register('/author', lambda:"HankelBao")
        DirectAPI.register('/', lambda:"DIDSYS API System")


class SubjectsAPI:
    def __init__(self, DirectAPI:DirectAPIRegister, mongo:MongoClient):
        self.subjects = mongo.db.subjects
        DirectAPI.register('/subjects', lambda:'Here are some APIs about subjects')
        DirectAPI.register('/subjects/all', self.subjects_all)
        DirectAPI.register('/subjects/add', self.subjects_add)
        DirectAPI.register('/subjects/del', self.subjects_del)
        
    def subjects_all(self) -> list:
        subjects_cursors = self.subjects.find()
        subjects = []
        for subject in subjects_cursors:
            subject.pop("_id")
            subjects.append(subject)
        return subjects

    def subjects_add(self, name:str, full_score:int) -> bool:
        self.subjects.insert({
            "name":name,
            "full_score": full_score
        })
        return True

    def subjects_del(self, name:str) -> bool:
        self.subjects.delete_many({'name':name})
        return True

class ClassesAPI:
    def __init__(self, DirectAPI:DirectAPIRegister, mongo:MongoClient):
        self.classes = mongo.db.classes
        DirectAPI.register('/classes', lambda:'Here are APIs about classes')

    def add(self, name:str) -> bool:
        self.classes.insert({
            "name":name
        })
        return True

class InspectorsAPI:
    def __init__(self, DirectAPI:DirectAPIRegister, mongo:MongoClient):
        self.inspectors = mongo.db.inspectors
        DirectAPI.register('/inspectors', lambda:'Here are APIs about inspectors')

class RecordsAPI:
    def __init__(self, DirectAPI:DirectAPIRegister, mongo:MongoClient):
        self.records = mongo.db.records
        DirectAPI.register('/records', lambda:'Here are APIs about records')

class AdminsAPI:
    def __init__(self, DirectAPI:DirectAPIRegister, mongo:MongoClient):
        self.admins = mongo.db.admins
        DirectAPI.register('/admins', lambda:'Here are APIs about admins')
        
