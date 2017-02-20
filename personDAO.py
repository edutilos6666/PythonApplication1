class PersonDAO:
    __container = {}
    def save(self, person):
        self.__container[person.get_id()] = person ;

    def update(self, id, newPerson):
        self.__container[id] = newPerson

    def delete(self, id):
        del self.__container[id]

    def find_by_id(self, id):
        return self.__container[id]


    def find_all(self):
        return list(self.__container.values())

