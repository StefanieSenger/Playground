# examples from the Python guide: https://docs.python.org/3/howto/descriptor.html

# descriptor that returns a constant
class Ten: # Descriptor class
    def __get__(self, obj, objtype=None):
        return 10

class A:
    x = 5
    y = Ten() # to use the descriptor, it must be stored as a class variable in another class

instance_a = A()
print(instance_a.x)
print(instance_a.y) # value 10 is computed on demand, not stored in A or instance_a

print("###########################################")

# dynamic lookup
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

dirname = os.path.join("..", os.path.dirname(__file__))
directory = Directory(dirname)
print(directory.size)

print("###########################################")

# Managed attributes
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value

class Person:

    age = LoggedAgeAccess()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()

person_a = Person("anna", 27)
print(person_a.name)
print(person_a.age)
print(person_a.birthday())              # this also outputs None, because the birthday method doesn't have a return statement

print("###########################################")
