# min heap implementation
import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize;
        self.Heap = [0]*(self.maxsize + 1)
        self.size = 0
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # function to return parent
    def parent(self,pos):
        return pos // 2

    # function to return left child
    def leftChild(self,pos):
        return 2*pos

    #function to return right child
    def rightChild(self,pos):
        return (2 * pos) + 1

    def isLeaf(self,pos):
        if pos >=(self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self,fpos,spos):
        self.Heap[spos],self.Heap[fpos] = self.Heap[fpos],self.Heap[spos]

    def minHeapify(self,pos):
        #if the node is non leaf and greater than any of its child
        if not self.isLeaf(pos):
            if(self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                if(self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]):
                    self.swap(pos,self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos,self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self,val):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = val

        current = self.size

        while(self.Heap[current] < self.Heap[self.parent(current)]):
                self.swap(current, self.parent(current))
                current = self.parent(current)

    

    def Print(self):
        for i in range(1, (self.size //2)+1):
            print("parent :" + str(self.Heap[i]) + "Left Child" +  str(self.Heap[2 * i]) + "Right Child" + str(self.Heap[2 * i + 1]))

    def extractMin(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -=1
        self.minHeapify(self.FRONT)
        return popped

# driver code

if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)

    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.insert(19)
    minHeap.insert(6)

    minHeap.Print()

    print("The min val is " + str(minHeap.extractMin()))



