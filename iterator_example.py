## ITERATORS

# Lists are iterable, because in their class definition, they have the __iter__() method
nums = [1, 2, 3]

for num in nums:
    print(num)

print(dir(nums)) # lists all the methods availaible to an object
                 # lists have the __iter__() method, and are thus iterable
                 # lists though don't have a __next__() method --> they are not iterators

# Creating an interator object of our list (as an alternative to the for loop)
i_nums = nums.__iter__() # more common way to call this would be: iter(nums)
print(i_nums)
print(dir(i_nums))

# Iterator is an object with a state (pointer), so that each time next method is called, the iterator returns the next object
print(next(i_nums)) # 1
print(next(i_nums)) # 2
print(next(i_nums)) # 3
print(next(i_nums)) # Oops: StopIteration Exception (this is that the for loop swallows)

# Writing out the functionality of a for loop
while True:
    try:
        item = next(i_nums)
    except StopInteration:
        break


# Credits: Corey Schafer @ https://www.youtube.com/watch?v=jTYiNjvnHZY