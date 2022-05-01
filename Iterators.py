## ITERATORS

# Lists are iterable, because in their class definition, they have the __iter__() method
nums = [1, 2, 3]

for num in nums:
    print(num)

print(dir(nums)) # lists all the methods availaible to an object