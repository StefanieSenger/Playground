print("\n######### playing with object class #########")

object1 = object()

print([key for key, _ in object.__dict__.items()])

#raises error, despite having `__setattr__`
try:
    object1.attribute = "attribute"
except AttributeError as e:
    print(f"AttributeError: {e}")

print(object1.__class__)
print(object.__class__)
print(object.__class__.__class__)

class X:
    pass

object2 = X()
print(object2.__class__)
print(X.__class__)

print("\n######### playing with __init__ #########")

# we don't need an __init__, but it's more explicit
class Rectangle:
    def area(self):
        return self.length* self.width

r = Rectangle()
r.length, r.width = 12,4
print(r.area())

print("\n######### playing with Enum #########")

from enum import Enum

# used for making short types, that can only appear once
class Suit(str, Enum):
    Club = "club"
    Diamond = "diamond"
    Heart = "heart"
    Spade = "spade"

print(repr(Suit.Club))
print(Suit.Heart.value)
print(list(Suit))

# the value cannot be changed
try:
    Suit.Diamond = "d"
except AttributeError as e:
    print(f"AttributeError: {e}")
# though the objects are still mutable, by adding attributes
