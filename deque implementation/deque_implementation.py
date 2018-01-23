## Defining Deque Class to implement Deque operations
## Deque is somehow both FIFO(First-In, First-Out) and LIFO(Last-In, First-Out) Data Structure 

## I am going to reduce amount of comments for this code since they are exactly like Stack + Queue combined. 
## Refer to my Stack and Queue codes if you're lost

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

## Testing

d = Deque()
d.addFront('hello')
d.addRear('word')
print(d.size())
print(d.removeFront() + ' ' + d.removeRear())
print(d.size())
