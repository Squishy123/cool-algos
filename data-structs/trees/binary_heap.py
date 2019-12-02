# Binary heap implementation for a min-heap
class BinaryHeap():
    # create a new binary heap
    def __init__(self):
        self.items = [0]

    # length of heap
    def __len__(self):
        return len(self.items)

    # insert an item and perc it into the right spot
    def insert(self, k):
        self.items.append(k)
        self.percUp(len(self))

    # delete the minimum child and return it
    def deleteMin(self):
        #save min elem
        retVal=self.items[1]
        #swap min position to last position
        self.items[1] = self.items[len(self)]
        self.items.pop()
        #percdown values
        self.percDown(1)
        return retVal

    # create a heap from a list of keys
    def buildHeap(self, alist):
        # set i to middle
        i=len(alist) // 2
        # append list to items
        self.items=[0] + alist
        while(i > 0):
            self.percDown(i)
            i-=1

    # percolate up items not in the right position
    def percUp(self, i):
        # while position is not 0
        while(i // 2 > 0):
            # if parent is greater than child/current
            if(self.items[i//2] > self.items[i]):
                # swap
                self.items[i//2], self.items[i] = self.items[i], self.items[i//2]

            # increment i
            i //= 2

    # percolate down items not in the right position    
    def percDown(self, i):
        # while position does not exceed heap
        while(i * 2 <= len(self)):
            #determine the minimum child
            mc = self.minChild(i)
            #check if current is greater than child
            if(self.items[i] > self.items[mc]):
                # if so swap
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            
            # increment i
            i=mc
               

    # determines the smallest child node and returns the position
    def minChild(self, i):
        # check if right child is bigger than current, if so then return left child
        # since parent is <= child
        if i * 2 + 1 > len(self):
            return i * 2

        # if left is smaller than right
        if self.items[i*2] < self.items[i*2+1]:
            return i * 2

        return i * 2 + 1
