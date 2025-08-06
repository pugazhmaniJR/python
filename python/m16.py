   # Decorators – Functions that modify other functions

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


 # Generators – Memory-efficient iterators using yield

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)


 # Metaclasses – Classes of classes (used for class customization)

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
