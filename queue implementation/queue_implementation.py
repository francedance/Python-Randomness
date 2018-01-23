## Defining Queue Class to implement Queue operations
## Queue is FIFO(First-In, First-Out) Data Structure Or (First-Come, First-Served)

class Queue(object):

    def __init__(self):
        ## Construction function of creating empty Queue
        self.items = []
    
    def isEmpty(self):
        ## Returns boolean value whether current Queue is empty or not
        return self.items == []

    def enqueue(self,item):
        ## Inserting an item into '0' index of Queue.
        ## Unlike Stack where we just appended an item to a list,
        ## Queue must be pushed to very first index to follow FIFO structure
        ## For example, enqueue of '1' into empty Queue is fine. 
        ## Now if you enqueue '2' into Queue using Stack method, your list would look like [1,2]
        ## So when you do pop() operation, it will remove '2' which isn't FIFO structure
        ## By inserting to 0 index, you can implement FIFO structure so your list would look like [2,1]
        ## And pop() operation will remove '1' which was inserted first than '2'
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

## Testing

print('Initializing Queue')
q = Queue()
print('Is Queue empty? ', q.isEmpty())
print('What\'s Queue\'s size? ' , q.size())
print('Enqueing value 1 into Queue')
q.enqueue(1)
print('Enqueing value 2 into Queue')
q.enqueue(2)
print('Is Queue empty? ', q.isEmpty())
print('What\'s Queue\'s size? ' , q.size())
print('Dequeing Queue')
print(q.dequeue())
print('Dequeing Queue')
print(q.dequeue())
print('Is Queue empty? ', q.isEmpty())
print('What\'s Queue\'s size? ' , q.size())

