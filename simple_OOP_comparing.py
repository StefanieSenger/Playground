# OOP exercise for comparing wealth among students

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
    def wealth(self):
        return 5*self.fives + 10*self.tens + 20*self.twenties
    def compare(self, other):
        self.other = other.name
        if self.wealth() > other.wealth():
            return(self.name)
        else:
            return other.name
        
bill = Student('Bill', 2, 30, 1)
susi = Student ('Susi', 4, 3, 3)

print(susi.wealth())
print(bill.wealth())
print(susi.compare(bill))