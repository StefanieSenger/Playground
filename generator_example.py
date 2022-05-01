# GENERATOR EXAMPLE

# Creating a generator function
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1     # do the same thing as iterators and are neater to read

nums = my_range(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)

# Credits: Corey Schafer @ https://www.youtube.com/watch?v=jTYiNjvnHZY