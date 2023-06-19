class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass

class Account():
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
        print(f'*** Created a bank account for {self.name} ***')

    def deposit(self, amount):
        if amount <= 0:
            raise AbortTransaction ('Amount must be positive. Order cancelled.')
            #print('You cannot deposit a negative amount. Order cancelled.')
            #return None

        self.balance += amount
        print(f'{self.name} added {amount} Euros to their bank account.')

        return self

    def withdraw(self, password, amount):
        if password != self.password:
            raise AbortTransaction ('Incorrect password.')
            #print('Sorry, incorrect password.')
            #return None

        if amount <= 0:
            raise AbortTransaction ('Amount must be positive. Order cancelled.')
            #print('You cannot withdraw a negative amount. Order cancelled.')
            #return None

        if (self.balance - amount) <= 0:
            raise AbortTransaction ('You cannot withdraw more than you have. Order cancelled.')
            #print('You cannot withdraw more than you have. Order cancelled.')
            print(f'{self.name} withdrew {amount} Euros form their bank account.')
        else:
            self.balance -= amount
            print(f'{self.name} withdrew {amount} Euros form their bank account.')

        return self

    def check_balance(self, password):
        if password != self.password:
            raise AbortTransaction ('Incorrect password.')
            #print('Sorry, incorrect password.')
            #return None

        return print(f'{self.name}, you have {self.balance} Euros in your bank account.')
