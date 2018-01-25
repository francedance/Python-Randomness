## Defining a class of singly linked list
class Node(object):
    ## Constructor function
    def __init__(self,value):

        ## Defining a node 
        self.value = value
        ## Initially, we set next node to None
        self.nextnode = None

## Creation of node 'a' with value 1 
## So it looks like [a|1]
a = Node(1)
## Creation of node 'b' with value 2
## So it looks like [b|2]
b = Node(2)
## Creation of node 'c' with value 2
## So it looks like [c|3]
c = Node(3)

## Defining nextnode
## We're defining nextnode of 'a' node to be 'b' node
## [a|1] -> [b|2]
a.nextnode = b
## We're defining nextnode of 'b' node to be 'c' node
## [a|1] -> [b|2] -> [c|3]
b.nextnode = c

## Print node 'a' value
print(a.value)
## Print node 'b' value
print(b.value)
## Print node 'c' value , since it's the nextnode of node 'b'
print(b.nextnode.value)