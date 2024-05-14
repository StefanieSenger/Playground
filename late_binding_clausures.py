""" In Python, variables used in a closure (for instance a lambda function) are bound at the time the
function is executed, not when it is defined. """

def create_multipliers():
    return [lambda x : i * x for i in range(5)] # create a list of lambda functions

# create_multipliers() returns a list of functions:
print(type(create_multipliers())) # <class 'list'>

# this is the first element:
print(create_multipliers()[0]) # <function create_multipliers.<locals>.<lambda> at 0x75f9d03dccc0>

# we can pass an argument into it, that gets evaluated to x:
print(create_multipliers()[0](2)) # 8

# Since i is shared among all lambda functions and its final value is 4, each lambda
# function effectively multiplies 2 by 4, resulting in 8:
for multiplier in create_multipliers():
    print(multiplier(2), end=", ") # 8, 8, 8, 8, 8
print('')

"""The variable i is bound to different values (0, 1, 2, 3, 4) during the loop
execution. Due to late binding in closures, each lambda function captures the final
value of i (4) when they are executed. This illustrates how closures and late binding
work together in Python to create functions that "remember". """

# same result here:
def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier) # not calling, only transporting the function, 
        # somehow, the final state of `i` gets transported as well

    return multipliers

for multiplier in create_multipliers():
    print(multiplier(2), end=", ") # 8, 8, 8, 8, 8
print('')


""" If we want to avoid this, we need to pass i into the (lambda) function, but as a
default argument (see `mutable_default_arguments.py`): """

def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)] # create a list of lambda functions

for multiplier in create_multipliers():
    print(multiplier(2), end=", ") # 0, 2, 4, 6, 8
print('')

# Alternatively, we can use functools.partial:
from functools import partial
from operator import mul

def create_multipliers():
    return[partial(mul, i) for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2), end=", ") # 0, 2, 4, 6, 8
print('')