from pymongo import MongoClient

class MongoConnection():
    def __init__(self, database_name):
        if database_name:
            client=MongoClient('localhost', 27017) 
            self.db=client[database_name]
    
    def get_db(self):
        if self.db:
            return self.db

class Document():
    def __init__(self, mongo_connection, document_name, fields_names, index_names=None):
        db = mongo_connection.get_db()
        self.doc = db.__getattr__(document_name)

        self.fields = {}
        for field_name in fields_names:
            self.fields[field_name] = None

        self.index_names = index_names
        

    def check_exist(self):
        if not self.index_names:
            return False
        
        index_condition = {}
        for index_name in self.index_names:
            index_condition[index_name] = self.fields[index_name]
        
        if self.doc.find_one(index_condition):
            return True
        else:
            return False

    def save(self):
        if self.check_exist():
            print("Update is needed")
        else:
            self.doc.insert(self.fields)
        