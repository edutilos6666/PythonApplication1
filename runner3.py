import os
import sys
import random
import MySQLdb as mdb
from pymongo import MongoClient


def testMysql():
    conn = mdb.connect("localhost", "root", "", "test")
    cur = conn.cursor()
    cur.execute("select * from  person")

    rows = cur.fetchall()
    for row in rows:
        print(row)


class Worker:
    __id = None
    __name = None
    __age = None
    __wage = None
    __active = None

    def __init__(self, id, name, age, wage, active):
        self.__id = id
        self.__name = name
        self.__age =  age
        self.__wage = wage
        self.__active = active

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_wage(self, wage):
        self.__wage = wage

    def set_active(self, active):
        self.__active = active

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_wage(self):
        return self.__wage

    def is_active(self):
        return self.__active

    def toString(self):
        return "[{},{},{},{},{}]".format(self.__id , self.__name, self.__age, self.__wage, self.__active)



class WorkerDAO:
     __workerContainer = {}
     def saveWorker(self, worker):
         self.__workerContainer[worker.get_id()] = worker

     def updateWorker(self, id , worker):
         self.__workerContainer[id] = worker

     def removeWorker(self, id):
         del self.__workerContainer[id]

     def findWorkerById(self, id):
         return self.__workerContainer[id]


     def findAll(self):
         return self.__workerContainer.values()



def testWorkerDAO():
    dao = WorkerDAO()
    dao.saveWorker(Worker(1, "foo", 10 , 100.0, True))
    dao.saveWorker(Worker(2, "bar", 20 , 200.0, False))
    dao.saveWorker(Worker(3, "bim", 30, 300.0, True))
    all = dao.findAll()
    for w in all :
        id = w.get_id()
        name = w.get_name()
        age = w.get_age()
        wage = w.get_wage()
        active =w.is_active()
        str = "{}, {},{}, {}, {}".format(id, name, age, wage, active)
        print(str)


def testUserInput():
      name = None
      age = None
      wage = None
      active = None
      print("enter name: ")
      name = sys.stdin.readline().rstrip()
      print("enter age: ")
      age = sys.stdin.readline().rstrip()
      print("enter wage: ")
      wage = sys.stdin.readline().rstrip()
      print("enter active: ")
      active = sys.stdin.readline().rstrip()
      print("*** user infos***")
      print("name = " , name)
      print("age = " , age)
      print("wage = " , wage)
      print("active = " , active)


def testMysql2():
    host = "localhost"
    user = "root"
    password = ""
    dbName = "test"
    con = mdb.connect(host , user, password , dbName)
    cursor = con.cursor()
    #create table
    cursor.execute("drop table if exists PythonWorker")
    con.commit()
    cursor.execute("""create table if not exists PythonWorker (
  id bigint primary key ,
  name varchar(50) not null,
  age int not null ,
  wage double not null,
  active boolean not null
)""")

    con.commit()
    cursor.execute("insert into PythonWorker VALUES(%s,%s,%s,%s,%s)",("1", "foo", "10", "100.0", True))
    cursor.execute("""insert into PythonWorker VALUES(2, "bar", 20 , 200.0, False)""")
    print("executed successfully.")
    cursor.execute("select * from PythonWorker")
    con.commit()
    desc = cursor.description
    for d in desc:
        print(d[0], end = " ")
    print("")
    rows = cursor.fetchall()
    for row in rows:
        print(row)




def testFile():
    file = open("foo.txt", "w")
    print(file.mode)
    print(file.name)
    file.write("foo\n")
    file.write("bar")
    file.close()

    file = open("foo.txt", "r")
    print(file.mode)
    print(file.name)
    data = file.read()
    print(data)
    file.close()

    file = open("foo.txt", "r+")
    line = file.readline()
    while(line):
        print(line, end = "")
        line = file.readline()


def serialize(workerContainer, fileName):
    file = open(fileName, "w")
    for worker in workerContainer:
        id = worker.get_id()
        name = worker.get_name()
        age = worker.get_age()
        wage = worker.get_wage()
        active = worker.is_active()
        str = "{},{},{},{},{}\n".format(id, name, age, wage, active)
        file.write(str)
    file.close()

def deserialize(fileName):
   file =  open(fileName, "r")
   container = []
   line = file.readline().rstrip()
   while(line):
       splitted = line.split(",")
       worker = Worker(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4])
       container.append(worker)
       line = file.readline().rstrip()
   return container


def testSerialize():
    workerContainer = [
        Worker(1, "foo", 10, 100.0, True),
        Worker(2, "bar", 20, 200.0 , False),
        Worker(3, "bim", 30 , 300.0, True)
    ]

    fileName = "workers.txt"
    serialize(workerContainer, fileName)
    container2 = deserialize(fileName)
    for w in container2:
        print(w.toString())

def testMongoClient():
     client = MongoClient()
     client.drop_database("test")
     db = client["test"]
     workerColl = db["PythonWorker"]
     workerColl.drop()
     workerColl = db["PythonWorker"]
     workerColl.insert_one({"id": 1 , "name": "foo", "age": 10 , "wage": 100.0, "active": True});
     workerColl.insert_many([
         {"id": 2, "name": "bar", "age": 20, "wage": 200.0, "active": False},
         {"id": 3, "name": "bim", "age": 30, "wage": 300.0, "active": True}
     ]);


     worker = workerColl.find_one({"id": 1});
     print(worker["id"], worker["name"], worker["age"], worker["wage"], worker["active"])

     workerList = workerColl.find()
     for w in workerList:
         print(w["id"], w["name"], w["age"], w["wage"], w["active"])

     workerColl.update_one({"id": 1},{"$set":{"name": "newfoo"}})
     workerColl.update_one({"id":1} , {"$set": {"age": 66}})
     workerColl.update_one({"id":1}, {"$set": {"wage": 666.6}})
     workerColl.update_one({"id": 1}, {"$set": {"active": False}})
     #, "age": 66, "wage": 666.5, "active": False})


     worker = workerColl.find_one({"id": 1})
     print("after update")
     print(worker["id"], worker["name"], worker["age"], worker["wage"], worker["active"])
     #remove
     workerColl.remove({"id": {"$gt": 2}})
     print("after remove")
     workerList = workerColl.find().limit(2)
     for w in workerList:
         print(w["id"], w["name"], w["age"], w["wage"], w["active"])

def main():
    testMongoClient()


if __name__ == "__main__":
    main()



