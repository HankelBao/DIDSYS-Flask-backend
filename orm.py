from settings import *

def Field():
    return ""

def ListField():
    return []

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class EmbeddedDocument(dict, object, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        try:
            test_valid = kw['name']
        except KeyError:
            kw['name'] = ""
        for name, value in vars(self.__class__).items():
            try:
                test_valid = kw[name]
            except KeyError:
                if  name != "__table__" and name != "__doc__" and name != "__module__" :
                    kw[name] = value
        super(EmbeddedDocument, self).__init__(**kw)


    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class Document(EmbeddedDocument):
    def save(self):
        if mongo.db.__getattr__(self.__table__).find_one({"name": self['name']}):
            mongo.db.__getattr__(self.__table__).update(
                {"name": self['name']}, self)
        else:
            mongo.db.__getattr__(self.__table__).insert(self)

    @classmethod
    def find(cls, pk):
        rs = mongo.db.__getattr__(cls.__table__).find({"name": pk})
        return cls(**rs[0])
