from Account import Account, AbortTransaction

account_dict = {}
next_account_number = 0

# Instiantiating new bank accounts in a dict
mickeys_account = Account('Mickey Mouse', 'minniemouse', 40)
mickeys_account_number = next_account_number
account_dict[mickeys_account_number] = mickeys_account
next_account_number += 1

minnies_account = Account('Minnie Mouse', 'goofy:::my:::love120?%/B"%', 0)
minnies_account_number = next_account_number
account_dict[minnies_account_number] = minnies_account
next_account_number += 1

# Operations on the bank accounts in daily usage
print('')

try:
    account_dict[mickeys_account_number].withdraw('minniemouse', 50)
except AbortTransaction as error:
    print(error)

try:
    account_dict[mickeys_account_number].check_balance('minniemouse')
except AbortTransaction as error:
    print(error)

try:
    account_dict[mickeys_account_number].withdraw('minniemouse', 30).deposit(400)
except AbortTransaction as error:
    print(error)

try:
    account_dict[mickeys_account_number].check_balance('minniemouse')
except AbortTransaction as error:
    print(error)

try:
    account_dict[mickeys_account_number].deposit(100).withdraw('minniemouse', 50).check_balance('minniemouse')
except AbortTransaction as error:
    print(error)

print('')

try:
    account_dict[minnies_account_number].check_balance('somepassword%#?/&&')
except AbortTransaction as error:
    print(error)

try:
    account_dict[minnies_account_number].deposit(20).withdraw('goofy:::my:::love120?%/B"%', 10).withdraw('goofy:::my:::love120?%/B"%', 15).check_balance('goofy:::my:::love120?%/B"%')
except AbortTransaction as error:
    print(error)

try:
    account_dict[minnies_account_number].deposit(-10)
except AbortTransaction as error:
    print(error)
