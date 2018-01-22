## Defining Stack Class to implement Stack operations
## Stack is LIFO(Last-In, First-Out) Data Structure

class Stack(object):

    def __init__(self):
        ## Constructor function of creating a new stack
        self.items = []

    def isEmpty(self):
        ## Return Boolean value based on empty or not
        return self.items == []

    def push(self, item):
        ## Push operation of item into a stack
        self.items.append(item)

    def pop(self):
        ## Pop operation of popping item from a stack
        return self.items.pop()

    def peek(self):
        ## Peeking, Checking the last element that was pushed into a stack
        return self.items[len(self.items)-1]

    def size(self):
        ## Returns current size of stack
        return len(self.items)

## Testing Stack Operations

s = Stack() ## Initializing a Stack object
print(s.isEmpty()) ## Should return True at first place
s.push(1) ## Pushing 1 into Stack
s.push('Hello') ## Push 'Hello' String into Stack
s.push(4+2) ## Pushing 6 into Stack
print(s.peek()) ## Checking the last element that was pushed without popping, should return 6
s.pop() ## Popping last element that was pushed (6)
s.pop() ## Popping ('Hello')
s.pop() ## Popping (1)
print(s.isEmpty()) ## It should be Empty! 
