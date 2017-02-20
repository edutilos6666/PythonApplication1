from person import Person
from personDAO import PersonDAO
import os
import sys
import random
from sys import stdin, stdout, stderr
import re




dao = PersonDAO()
dao.save(Person(1, "foo", 10 , 100.0 , True))
dao.save(Person(2, "bar", 20, 200.0 , False))


list = dao.find_all()
for p in list :
    print(p.toString())

dao.update(1, Person(1, "newfoo", 66, 666.6, False))

p = dao.find_by_id(1)

assert 1 == p.get_id()
assert "newfoo" == p.get_name()
assert 66 == p.get_age()
assert 666.6 == p.get_wage()
assert False == p.is_active()

list = dao.find_all()
assert  2 == len(list)

dao.delete(1)
list = dao.find_all()
assert 1 == len(list)

dao.delete(2)
list = dao.find_all()
assert 0 == len(list)


i = 0
while(i < 5) :
    rand = random.randrange(0 , 100)
    print(rand)
    i += 1





# print("insert name: ")
# name =  stdin.readline().rstrip('\n')
# print("insert age: ")
# age = int(stdin.readline())
# print("insert wage: ")
# wage = float(stdin.readline())
#
# print("Name = {}, age = {}, wage = {}".format(name, age, wage))
# print("Name =", name, "age = ", age , "wage = ", wage)



print("insert name , age, wage : ")
input = stdin.readline().rstrip('\n')
splitted = re.compile("\s*,\s*").split(input)
name = splitted[0]
age = int(splitted[1])
wage = float(splitted[2])
print("Name =", name, "age = ", age , "wage = ", wage)





