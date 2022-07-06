# OOP exercise: the life of an orange tree

import random

class OrangeTree(object):
    def __init__(self, age, height, fruits, dead):
        self.age = age
        self.height = height
        self.fruits = fruits
        self.dead = dead
    def one_year_passes(self):
        self.age += 1
        self.fruits = 0
        if self.dead == True:
            pass
        else:
            if self.age > 100:
                self.dead = True
            elif (self.age > 49) and (self.age < 100):
                #random.seed(1000)
                self.dead = (self.age*random.random() > 50)
                #random.seed(1000)
                #print(self.age*random.random())
            else:
                pass
        if self.dead == False:
            if self.age <= 10: 
                self.height += 1
            if (self.age >= 15) or (self.age < 5):
                pass
            elif self.age >= 10:
                self.fruits += 200
            else:
                self.fruits += 100
    def pick_a_fruit(self):
        if self.fruits > 0:
            self.fruits -=1

test_tree = OrangeTree(0, 0, 0, False)

for year in range(100):
    test_tree.one_year_passes()
    print('Age:', test_tree.age, 'Height:', test_tree.height, 'Fruits:', test_tree.fruits, 'Dead:', test_tree.dead)