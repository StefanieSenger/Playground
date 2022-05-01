# Building a Class that is iterable

class MyRange:

    # objects shall behave like the range function
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # makes the objects iterable
    def __iter__(self):
        return self

    # makes the object an iterator
    def __next__(self):      # defining the inner logic of the next pointer
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current       # returns currently pointed to item within the iterator and moves pointer to the next one

# instantiating an iterable object, that's also an interator (you can call the next()-method on)
nums = MyRange(1, 10)

#for num in nums:
#    print(num)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# --> advantage of iterables: no need to store data in a data structure, defining how to go iterate through something in a loop is enough

# Credits: Corey Schafer @ https://www.youtube.com/watch?v=jTYiNjvnHZY