class Example():
    def __init__(self, starting_value):
        self._starting_value = starting_value

    @property
    def x(self): # getter method
        return self._starting_value

    @x.setter
    def x(self, new_value): # setter method
        self._starting_value = new_value

example = Example(1)

print(example.x)
example.x = 2 # instead of `example.x(2)`, because it's a property
print(example.x)
print(example.__dict__)


class Example2:
    def __init__(self):
        self._value = 0

    @property
    def x(self):
        return self._value

    @x.setter
    def x(self, new_value):
        if new_value < 0:
            raise ValueError("Invalid value: Value must be non-negative.")
        self._value = new_value

example = Example2()

try:
    example.x = -1
except ValueError as e:
    print("Error:", e)
