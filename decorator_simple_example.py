# Decorators: Simple Examples

# one function taking another function as an input and wrapping it into a wrapper
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    
    return wrapper

def f():
    print('Hello')

# calling the second function (f) as an input into another function (f1)
f = f1(f)         #<-- this can be substituted by a decorator

f()

# the same functionality using a decorator
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    
    return wrapper

@f1
def f():
    print('Hello')

f()

# similar functionality but with parameters (the problem to solve is that we don't always want to manually take care that func() and f() have the same parameters
def f1(func):
    def wrapper(*args, **kwargs):    #these are placeholders for an undefined number of arguments and parameters
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    
    return wrapper

@f1
def d(a, b=9):
    print(a, b)

d('Hi')

# returning values from decorated functions
def f1(func):
    def wrapper(*args, **kwargs):  
        print("Started")
        val = func(*args, **kwargs)  # saving the value, so that what needs to be executed afterwards, gets still done
        print("Ended")
        return val
    
    return wrapper  # the wrapper then returns val

@f1                   # we can use the same decorators on more than one function at a time
def add(x,y):
    return x+y

print(add(4,5))

# Credits: Tim @ https://www.youtube.com/watch?v=r7Dtus7N4pI 