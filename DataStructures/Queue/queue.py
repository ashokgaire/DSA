'''
A Queue is a linear structure which follows a particular order in which the operations are performed. 
The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 
The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; 
in a queue, we remove the item the least recently added.


Operations on Queue:

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
Front: Get the front item from queue.
Rear: Get the last item from queue. 
'''


class Queue:

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity
        self.capacity = capacity

    # queue is ful when size becomes equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
    
    # add item to queue
    # it changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item 
        self.size = self.size + 1
        print(" %s enqueued to queue" %str(item))
    

    # remove item
    def Dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        
        print("%s dequeued from queue" %str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
        
    def que_front(self):

        if self.isEmpty():
            print("Queue is empty")
        
        print("Front item is ",self.Q[self.front])

    def que_rear(self):
        if self.isEmpty(): 
            print("Queue is empty") 
        print("Rear item is",  self.Q[self.rear]) 
  
  
# Driver Code 
if __name__ == '__main__': 
  
    queue = Queue(30) 
    queue.EnQueue(10) 
    queue.EnQueue(20) 
    queue.EnQueue(30) 
    queue.EnQueue(40) 
    queue.Dequeue() 
    queue.que_front() 
    queue.que_rear() 
    
        
