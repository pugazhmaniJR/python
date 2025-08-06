class Person:
  def __init__(self, fname, lname,age,comingfrom):
    self.firstname = fname
    self.lastname = lname
    self.Age=age
    self.Comingfrom=comingfrom
  def printname(self):
    print(self.firstname, self.lastname,self.Age,self.Comingfrom)
 
one= Person("Pugazh","Mani",20,"Uthiramerur")
one.printname()

import json

x='{"name":"pugazh","age":"20","work":"zenjade"}'

y=json.loads(x)
print(y)

one={
  "name":"Luffy",
  "names":"zoro",
  "namess":"sanji"
  }
print(len(one))



two=("apple","graps","mango","orange")
print(len(two))


import datetime

x = datetime.datetime.now()
print(x)

x=lambda a,b: a/b
print(x(10,78))



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
 



