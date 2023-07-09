'''exercise from Luciano Ramalho: Fluent Python, chapter 1
https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/data-model.ipynb'''

import math

class Vector:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__ (self, other):
        '''vector addition'''
        if type(other) != type(self):
            return None
        return Vector(self.num1 + other.num1, self.num2 + other.num2)

    def __abs__(self):
        '''length of vector'''
        return math.sqrt(self.num1**2+self.num2**2)

    def __mul__(self, number):
        '''scalar multiplication'''
        return Vector(self.num1 * number, self.num2 * number)

    def __str__(self):
        '''representation when printing object'''
        return f"Vector({self.num1}, {self.num2})"

    def __repr__(self):
        '''representation of object, also works with print'''
        '''"!r" is used to represent attributes in their original data type (int not str)'''
        return f'Vector({self.num1!r}, {self.num2!r})'

    def __bool__(self):
        '''False if magnitude of vector is 0, True otherwise'''
        return bool(abs(self))


v1 = Vector(2,4)
v2 = Vector(2,1)

v3 = v1 + v2

print(v3)
print(abs(v3))
print(v3 * 2)
print(bool(v3))
