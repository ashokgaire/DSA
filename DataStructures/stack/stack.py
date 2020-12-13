'''
Stack is a linear data structure which follows a particular order in which the operations are performed.
 The order may be LIFO(Last In First Out) or FILO(First In Last Out).

Implementation: 
There are two ways to implement a stack: 

    Using array
    Using linked list


'''

# implementation using array

#Used to return -infinite when stack is empty
from sys import maxsize

# function to create a stack.

def createStack():
    stack = []
    return stack 

def isEmpty(stack):
    return len(stack) == 0

#add an item to stack
#o(1) time
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

#remove a item from stack
def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1) #return minus infinite
    return stack.pop()

# retrun top of the stack without removing it
def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize - 1)
    return stack[len(stack) -1]

stack = createStack()
push(stack, str(10))
print(pop(stack) + " popped from stack")

'''
Pros: Easy to implement. Memory is saved as pointers are not involved. 
Cons: It is not dynamic. It doesn’t grow and shrink depending on needs at runtime.
'''



#impementation using linkist

#node cass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.root
        self.root = newNode
        print(data + "pushed to stack")
    
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data


'''
Pros: The linked list implementation of stack can grow and shrink according to the needs at runtime. 
Cons: Requires extra memory due to involvement of pointers.
'''