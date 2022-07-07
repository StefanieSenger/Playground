# simple OOP inheritance exercise

class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories	
    def healthy(self):
        if self.calories < 200:
            return True
        else:
            return False
    def delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        self.flavor = flavor
        super().__init__(name, calories)
    def delicious(self):
        if (self.flavor == 'black licorice'):
            return not (super().delicious())
        else:
            return super().delicious()

cherry_cake = Dessert('cherry cake', 300)
print(cherry_cake.healthy())
print(cherry_cake.delicious())
cherry_bean = JellyBean('jelly-bean', 20, 'cherry')
print(cherry_bean.flavor)
print(cherry_bean.delicious())
licorice_bean = JellyBean('jelly-bean', 20, 'black licorice')
print(licorice_bean.flavor)
print(licorice_bean.delicious())