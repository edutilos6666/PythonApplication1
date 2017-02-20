from person import Person
from personDAO import PersonDAO
import sys
import os
import random
from sys import stdin , stdout , stderr
import re




pattern = "\s*,\s*"

def to_boolean(x):
    #print(x.rstrip('\n').lower())
    #print(x.rstrip('\n').lower() in ("True", "true", "1", "t"))
    return x.rstrip('\n').lower() in ("True", "true", "1", "t")

to_boolean("True")

dao = PersonDAO()

def save_person():
    print("insert id , name, age, wage, active of person: ")
    input = stdin.readline()
    splitted = re.compile(pattern).split(input)
    id = int(splitted[0])
    name = splitted[1]
    age = int(splitted[2])
    wage = float(splitted[3])
    active = to_boolean(splitted[4])
    dao.save(Person(id, name, age, wage, active))

def update_person():
    print("insert id , name, age, wage , active of person: ")
    input = stdin.readline()
    splitted = re.compile(pattern).split(input)
    id = int(splitted[0])
    name = splitted[1]
    age = int(splitted[2])
    wage = float(splitted[3])
    active = to_boolean(splitted[4])
    dao.update(id, Person(id, name, age, wage, active))

def delete_person():
    print("insert id of person to be deleted: ")
    id = int(stdin.readline())
    dao.delete(id)


def find_by_id():
    print("insert id of person to be found: ")
    id = int(stdin.readline())
    p = dao.find_by_id(id)
    print(p.toString())

def find_all():
    people = dao.find_all()
    for p in people:
        print(p.toString())



menu = """
1 -> save person
2 -> update person
3 -> delete person
4 -> find by id
5 -> find all
6 -> break
"""
while(True):
    print(menu)
    answer = int(stdin.readline())
    if(answer == 1):
        save_person()
    elif(answer == 2):
        update_person()
    elif(answer == 3):
        delete_person()
    elif(answer == 4):
        find_by_id()
    elif(answer == 5):
        find_all()
    else :
        break