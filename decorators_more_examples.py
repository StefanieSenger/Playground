# Decorators: Practical Examples

# decorator as a method
def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print('run')

t = Test()
t.decorated_method()

# very common timer decorator that keeps track of how long a function executes
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print('Function took:', time.time() - before, 'seconds')
    
    return wrapper

@timer
def run():
    time.sleep(2)   # delaying two seconds (on purpose)

run()

# Credits: Tim @ https://www.youtube.com/watch?v=r7Dtus7N4pI 