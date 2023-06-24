class Stack():

    def __init__(self):
        self.stack_list = []

    def push(self, ele):
        self.stack_list.append(ele)
        return self

    def pop(self):
        self.stack_list = self.stack_list[:-1]
        return self

stack = Stack()

print(stack.stack_list)
stack.push(1).push(2).push(3)
print(stack.stack_list)
stack.pop().pop()
print(stack.stack_list)
stack.pop()
print(stack.stack_list)
stack.pop() # actually, should raise an IndexError when trying to pop more than there is
print(stack.stack_list)
