## Python implementation of Binary Min Heap using List 
class BinaryHeap:
    ## Constructor function for Binary Min Heap
    def __init__(self):
        ## We put 0 in their so we can easily play with number division
        self.heapList = [0]
        ## Current size of Heap list
        self.currentSize = 0

    ## Also known as Up-Heap operation (bubble-up, percolate-up, sift-up...)
    ## Since we're doing Min Heap, you can't just insert a value into a tree and call it 'done'!
    ## The parent of children should be less than its child. Meaning, Root value is the smallest of all.
    ## PercUp function will basically help us maintain sorted binary tree when inserting

    ## i = current index value of node being inserted
    def percUp(self,i):

        ## If it is initial isnertion (root), it will bypass this while loop
        ## If it is second insertion, we have to compare it with current parent. 
        ## Basically every other node being inserted will go through while loop except Root node
        while i // 2 > 0:

            ## This is the comparision if current inserting value is less than its parent
            if self.heapList[i] < self.heapList[i // 2]:

                ## If current value is less, we want to sort the tree!
                ## We make tmp variable to store its parent's value
                tmp = self.heapList[i // 2]
                ## Simply override its parent's value with its value
                self.heapList[i // 2] = self.heapList[i]
                ## Switching action between its parent and its value
                self.heapList[i] = tmp
            ## By setting i to i // 2, we can traverse back upto Root and check
            i = i // 2

    ## Insertion function, where k = value to be added
    def insert(self,k):

        ## Append inserting value into a list
        self.heapList.append(k)
        ## Increment the current size
        self.currentSize = self.currentSize + 1
        ## Perform Percolate-Up operation on a tree using currentSize
        self.percUp(self.currentSize)

    ## This is extraction function of smallest (if min-heap) or largest (if max-heap)
    def delMIn(self):
            ## The idea is similar to insert() but now we're removing. 
            ## Note, smallest or largest will always exist on root, [1] in our list
            retval = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(1)
            return retval

    ## This is similar to percUp but slight more complicate. 
    ## It is quiet hard to explain evey step of the code so just refer to Binary Heap's insert/extract method
    def percDown(self,i):

        while (i * 2) <= self.currentSize:

            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:

                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    ## Function to find the smallest child inside entire tree. It will support percDown() function   
    def minChild(self,i):

            if i * 2 + 1 > self.currentSize:

                return i * 2
            else:

                if self.heapList[i*2] < self.heapList[i*2+1]:
                    return i * 2
                else:
                    return i * 2 + 1

    def buildHeap(self,alist):
            i = len(alist) // 2
            self.currentSize = len(alist)
            self.heapList = [0] + alist[:]
            while(i > 0):
                self.percDown(i)
                i = i -1 

## Testing

test = BinaryHeap()
print(test.heapList)
print(test.currentSize)

## Inserting into a tree 

print('Inserting root 3')
test.insert('3')
print('Inserting 2')
test.insert('2')
print('Inserting 4')
test.insert('4')
print('Inserting 1')
test.insert('1')
## test.insert('5')

print('Current min heaplist looks like: ')
print(test.heapList)