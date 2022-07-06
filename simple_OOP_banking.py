# OOP exercise from https://www.codewars.com/kata/5a03af9606d5b65ff7000009/python

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    def withdraw(self, subtracted):
        self.subtracted = subtracted
        if self.balance - self.subtracted >= 0:
            self.balance = self.balance - self.subtracted
            return f'{self.name} has {self.balance}.'
        else:
            raise ValueError(f"{self.name} doesn't have enough money.")
    def check(self, other_user, money):
        self.other_user = other_user.name
        self.money = money
        if other_user.checking_account == True:
            if other_user.balance - self.money >= 0:
                self.balance = self.balance + money
                other_user.balance = other_user.balance - money
                return f'{self.name} has {self.balance} and {self.other_user} has {other_user.balance}.'
            else:
                raise ValueError(f"{other_user.name} doesn't have enough money.")
        else:
            raise ValueError(f"{other_user.name}s checking_account is disabled.")
    def add_cash(self, money_to_add):
        self.money_to_add = money_to_add
        self.balance = self.balance + self.money_to_add
        return f'{self.name} has {self.balance}.'
   
Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Jeff.withdraw(2))
print(Joe.check(Jeff, 50))
print(Jeff.check(Joe, 80))
print(Jeff.check(Joe, 40))
print(Jeff.add_cash(20))