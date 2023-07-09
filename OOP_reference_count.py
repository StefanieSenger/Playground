# increasing and reducing the reference count of an object

import sys


class SomeClass:
    pass

# incrementing refcount
# refcount is always 1 higher, because of additional temporary reference by `sys.getrefcount()` intself
object1 = SomeClass()
print(f"refcount after instantiating object: {sys.getrefcount(object1)}")

object2 = object1
print(f"refcount after assinging another variable to object: {sys.getrefcount(object1)}")

def my_function(some_object):
    print(f"refcount after using object as an argument in a function: {sys.getrefcount(object1)}") # only increases refcount until function returns, increases it even by two
my_function(object1)

my_list = [1, 2, object1]
print(f"refcount after passing object into a list: {sys.getrefcount(object1)}")


# decrementing refcoun
object2 = None
print(f"refcount after re-assinging variable that was before pointing object: {sys.getrefcount(object1)}")

my_list.pop() # `remove()` and `del my_list` also work
print(f"refcount after deleting object from a list: {sys.getrefcount(object1)}")

object1 = None
print(f"refcount after deleting the last reference (now refers to the None value): {sys.getrefcount(object1)}")
