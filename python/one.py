
person=15

if(person>18):
    print("HE IS DIED, but the code is work")
else:
   print("HE IS ALIVE , but the code doesn't work ")

 
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")
  
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford","Mustang")      
boat1 = Boat("Ibiza","Touring 20") 
plane1 = Plane("Boeing","747")     

for hii in (car1, boat1, plane1):
  hii.move()


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

oneset = {"apple", "banana", "cherry", "apple"}

print(oneset)

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["city"])