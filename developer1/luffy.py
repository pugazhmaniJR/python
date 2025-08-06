x=lambda a,b : a/b
print(x(5,87))


one={
    "name":"peter",
    "age":"23",
    "from":"finland"
}
print(len(one))


country=("brazil","iceland","poland","france","spain","germeny")
football=iter(country)
print(next(football))


import json

x='{"name:":"neymar","age":"34","700"}'
y=json.dumps(x)
print(y)


import json

v='{"name:":"neymar","age":"34","goal":"700"}'
x=json.loads(v)
print(x)


import datetime

x = datetime.datetime.now()
print(x)


month =1
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 1:
    print("its new year")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x)


BMW = {
  "brand": "BMw Futhur",
  "model": "Mustang",
  "year": 1964
}
BMW.update({"year": 2027})
print(BMW)


def my_function(fname):
  print(fname + "JR")

my_function("Pugazh")


a=57
b=86
c=43

if a<c :
    print("there is no leave ")
elif b>=a:
    print("one leave in this month")
else :
    ("you can ask permission")


fruits = ["apple", "banana", "cherry","orange","mango"]
for x in fruits:
  print(len(x))
  

fruit = ["graps", "banana", "cherry","orange","mango"]
for x in fruit:
  print(x[0])
  

one= lambda x,y : x*y
print(one(4,8))








