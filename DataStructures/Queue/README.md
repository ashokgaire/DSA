### Queue
* A Queue is a linear structure which follows a particular order in which the operations are performed. 
* The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 
* The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; 
in a queue, we remove the item the least recently added.


## Operations on Queue:

* Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
* Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
* Front: Get the front item from queue.
* Rear: Get the last item from queue. 


##  Applications of Queue:
Queue is used when things don’t have to be processed immediatly, but have to be processed in First InFirst Out order like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.


* 1) When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
* 2) When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. Examples include IO Buffers, pipes, file IO, etc.


### Complexity Analysis:

    ## Time Complexity:

   * Operations              Complexity
   *  Enque(insertion)           O(1)
   * Deque(deletion)            O(1)
   * Front(Get front)           O(1)
   * Rear(Get Rear)             O(1)              

    Auxiliary Space: O(N).
    N is the size of array for storing elements.

### Pros of Array Implementation:

    Easy to implement.

### Cons of Array Implementation:

    Static Data Structure, fixed size.
    If the queue has a large number of enqueue and dequeue operations, at some point we may not we able to insert elements in the queue even if the queue is empty (this problem is avoided by using circular queue).

