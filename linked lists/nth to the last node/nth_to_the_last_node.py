## Defining our own class for Singly Linked List
class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

## Defining a function that finds nth node to the last 
## a = list that looks like this([a|1] -> [b|2] -> [c|3] -> [d|4] -> [e|5])
## If you run a nth_to_last_node(2,a) , meaning finding second to the last node of passed node
## Correct output should node [d|4] sincei it's the second to the last of the node list.

## Here, we just define a function caled 'nth_to_last_node' with argument 'n' and 'head'
def nth_to_last_node(n,head):

    ## The trick is to make two markers which the width of two markers are 'n' wide. 
    ## It is like moving a block whose width is 'n' through the node list
    ## Being that said, if a right_pointer hits the end of node list, that basically says that 
    ## left_pointer is the nth to the last node (the node we've been looking for!)

    ## Setting two marker's starting position (initializing)
    left_pointer = head
    right_pointer = head

    ## This is a for loop that actually define 'n' wide block between two markers
    for i in range(n-1):

        ## Just edge checking!
        if not right_pointer.nextnode:
            ## Raising an error
            raise LookupError('Error: n is large than the linked list')
        
        ## Defining 'n' width right pointer! 
        right_pointer = right_pointer.nextnode

    ## Traversing the node and syncing the movements of 2 markers we created before
    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
    
    ## When all the above procedures are done, simply return the 'nth to the last node' 
    return left_pointer


## Testing!
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print('The value of 2nd to the last node is: ', nth_to_last_node(2,a).value) ## Just printing the value of that node
    

