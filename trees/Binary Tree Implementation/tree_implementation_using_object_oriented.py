## Python implementation of BinaryTree using Object Oriented style

## Defining BinaryTree Class
class BinaryTree(object):

    ## Construction function (basically creating a root)
    def __init__(self,rootObj):

        ## key = just another term for root node
        self.key = rootObj
        ## By default, leftChild and rightChild is set to None
        self.leftChild = None
        self.rightChild = None

    ## Function to insert a node into left
    def insertLeft(self,newNode):
        
        ## Case if current root doesn't have any leftChild
        if self.leftChild == None:
            ## We create a new instance of BinaryTree and insert
            self.leftChild = BinaryTree(newNode)
        ## Case if current root have leftChild
        else:
            ## t is the new instance of Tree we want to insert but not yet!
            ## If there is curent leftChild, we want to push current one down depth
            t = BinaryTree(newNode)
            ## We want to set t's leftChild to be current leftChild (Pushing action!)
            t.leftChild = self.leftChild 
            ## Redefining Root's leftChild to be the new node we're inserted
            self.leftChild = t 

    ## Same idea for inserting to Right
    def insertRight(self,newNode):
        
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t 
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

## Testing
## Here, I am creating alphabet BinaryTree. 
"""
                    a
              b           c
          d      e     f     g
       ....    ....  ....    ....
       
"""
r = BinaryTree('a')

print('Current Root is: ', r.getRootVal())
r.insertLeft('b')
print('Current Root\'s LeftChild is: ', r.getLeftChild().getRootVal())
r.insertRight('c')
print('Current Root\'s RightChild is: ', r.getRightChild().getRootVal())
r.leftChild.insertLeft('d')
print('\'B\' Node\'s LeftChild is: ',r.getLeftChild().getLeftChild().getRootVal())
r.leftChild.insertRight('e')
print('\'B\' Node\'s RightChild is: ',r.getLeftChild().getRightChild().getRootVal())
r.rightChild.insertLeft('f')
print('\'C\' Node\'s LeftChild is: ',r.getRightChild().getLeftChild().getRootVal())
r.rightChild.insertRight('g')
print('\'C\' Node\'s RightChild is: ',r.getRightChild().getRightChild().getRootVal())