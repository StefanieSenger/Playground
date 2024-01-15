# some exercises around decorators
# credits Jonathan Fernandes @ https://www.linkedin.com/learning/python-decorators/

def make_posh(func):
    '''This is the function decorator.'''
    def wrapper():
        '''This is the function wrapper.'''
        print("+---------+")
        print('|         |')
        print(func())
        print('|         |')
        print("+---------+")
    wrapper.__name__ = func.__name__ # otherwise pfib.__name__ gets us the wrapper's name
    wrapper.__doc__ = func.__doc__  # alternative is to use wraps from functools
    return wrapper

@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

pfib()
print(pfib.__name__)
print(pfib.__doc__)

##############################################
from functools import wraps

def make_posh(func):
    '''This is the function decorator.'''
    @wraps(func)
    def wrapper():
        '''This is the function wrapper.'''
        print("+---------+")
        print('|         |')
        print(func())
        print('|         |')
        print("+---------+")
    return wrapper

@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

pfib()
print(pfib.__name__)
print(pfib.__doc__)

##############################################
from functools import wraps

def make_italic(func):
    """Wrapper that returns a string within HTML italic tags."""
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

def make_bold(func):
    """Wrapper that returns a string within HTML bold tags."""
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@make_bold
@make_italic
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

print(printfib())

##############################################

def munch(start, end):
    """Outer function that defines start and end position"""
    def do_munch(func):
        """Inner function that takes a func and wraps it"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """'Replaces' chars in string"""
            string_to_replace = func()
            new_string = string_to_replace[:start] + "x"*(end-start) + string_to_replace[end:]
            return new_string
        return wrapper
    return do_munch

@munch(1,4)
def fib():
    return 'Fibonacci'

print(fib())
