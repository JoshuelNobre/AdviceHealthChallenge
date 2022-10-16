class Vehicle():
    def __init__(self, model, collor, person ):
        self.__model = model
        self.__collor = collor
        self.__person = person

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):
        self.__model = model


    @property
    def collor(self):
        return self.__collor
    @collor.setter
    def collor(self, collor):
        self.__collor = collor


    @property
    def person(self):
        return self.__person
    @person.setter
    def person(self, person):
        self.__person = person
        