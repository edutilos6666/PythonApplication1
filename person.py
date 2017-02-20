class Person:
    __id = None
    __name = None
    __age = None
    __wage = None
    __active = None

    def __init__(self, id , name, age, wage, active):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__wage = wage
        self.__active = active


    def get_id(self):
        return self.__id


    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age = age


    def get_wage(self):
        return self.__wage


    def set_wage(self, wage):
        self.__wage = wage


    def is_active(self):
        return self.__active

    def set_active(self, active):
        self.__active = active


    def toString(self):
        str = "{}, {}, {}, {},{}".format(self.__id , self.__name, self.__age, self.__wage, self.__active)
        return str