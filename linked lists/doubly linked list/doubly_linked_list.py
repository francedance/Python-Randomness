## Defining class for Doubly Linked List (think of it as two-way Singly Linked List)
class Doubly_Linked_List(object):

    def __init__(self,value):
        ## Similar to Singly Linked List except that Doubly Linked List have previous node and next node in each node
        self.value = value
        self.next_node = None
        self.prev_node = None

## Just creating node a , node b, node c
## At this point they aren't linked!
a = Doubly_Linked_List(1)
b = Doubly_Linked_List(2)
c = Doubly_Linked_List(3)

## Linking node 'a' with node 'b'
a.next_node = b
## Telling node 'b' that its previous node is node 'a'
b.prev_node = a
## Telling node 'b' that its next node is node 'c'
## At this point node 'b' is tracking of both ends (previous and next)
b.next_node = c
## Telling node 'c' that its previous node is node 'b'
c.prev_node = b
## This is optional but you can make a LOOP like Linked List
## In this case, node 'c' is referring its next node to be node 'a'
c.next_node = a

print('Overall Look of Doubly Linked List: \n', a.value, '<=>', b.value, '<=>', c.value, '<=> Back to Beginning')
print('Node \'a\' :', a.value)
print('Node \'a\'\'s next node value:', a.next_node.value)
print('Node \'b\'\'s previous node value:', b.prev_node.value)
print('Node \'b\'\'s next node value:',b.next_node.value)
print('Node \'c\'\'s previous node value:',c.prev_node.value)
print('Node \'c\'\'s next node value:',c.next_node.value)

print('Now Inserting node \'x\' between node \'b\' and node \'c\' ')
## Trying to insert new node between node 'b' and node 'c'
x = Doubly_Linked_List(4)

## Reassigning node 'b' next node to be x, changed from pointing to node 'c'
b.next_node = x 
## Reassigning node 'c' previous node to be x, changed from pointing to node 'b'
c.prev_node = x

print('Overall Look of Doubly Linked List: \n', a.value, '<=>', b.value, '<=>', x.value, '<=>', c.value, '<=> Back to Beginning')
print('Node \'b\'\'s next node value:',b.next_node.value)
print('Node \'c\'\'s previous node value:',c.prev_node.value)

