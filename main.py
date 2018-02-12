from DirectAPIFramework import DirectAPIApp, DirectAPIRegister
from MongoOrm import MongoConnection
from APIs import RootAPI, SubjectsAPI, ClassesAPI, InspectorsAPI, RecordsAPI, AdminsAPI


if __name__ == '__main__':
    directApiRegister = DirectAPIRegister()
    mongo = MongoConnection('didsys')

    RootAPI(directApiRegister)
    SubjectsAPI(directApiRegister, mongo)
    ClassesAPI(directApiRegister, mongo)
    InspectorsAPI(directApiRegister, mongo)
    RecordsAPI(directApiRegister, mongo)
    AdminsAPI(directApiRegister, mongo)


    app = DirectAPIApp(8080, directApiRegister)
    app.run()
