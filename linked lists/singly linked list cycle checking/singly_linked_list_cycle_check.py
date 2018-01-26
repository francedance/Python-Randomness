## Defining our own class for Singly Linked List
class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

## Defining a function that checks if a passed Node has Cycle or NOT
def cycle_check(node):

    ## We going to use Race method. 
    ## We're basically creating 2 marker to traverse through a node we're passing
    ## The trick here is to let marker2 traverse twice faster than marker1
    ## So if there is a cycle in a node, marker2 will eventually same as marker1!
    marker1 = node
    marker2 = node

    ## Loop and traverse a node until marker2 hits ends
    while marker2 != None and marker2.nextnode != None:

        ## Marker1 is pointing to nextnode (normal speed)
        marker1 = marker1.nextnode
        ## Marker2 is pointing to nextnode.nextnode (twice speed of marker1)
        marker2 = marker2.nextnode.nextnode

        ## Case which there is CYCLE, return True
        if marker2 == marker1:
            return True
    ## If no CYCLE, return False
    return False

## Testing
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a ## Cycle here

x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z ## No Cycle here


print(cycle_check(a)) ## True
print(cycle_check(x)) ## False