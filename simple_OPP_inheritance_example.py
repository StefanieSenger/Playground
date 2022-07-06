# simple inheritance example

class Dog:
    def bark(self):
        print("woof woof")
# Do not modify the code above

class GermanShepherd(Dog):
    def __init__(self):
        super().bark()
         
german_shepherd = GermanShepherd()
german_shepherd.bark()