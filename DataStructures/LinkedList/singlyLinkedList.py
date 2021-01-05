"""
Like arrays, Linked List is a linear data structure. 
Unlike arrays, linked list elements are not stored at a contiguous location; 
the elements are linked using pointers

Why Linked List?
Arrays can be used to store linear data of similar types, but arrays have the following limitations.
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. 
Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted. 


Representation:
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head.
 If the linked list is empty, then the value of the head is NULL.
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node
"""



#Node class
class Node:
    # Function to initialize the node object

    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    

    # Insertion
    '''
    1) At the front of the linked list 
    2) After a given node. 
    3) At the end of the linked list.
    ''' 

    # Function to insert a new node at the beginning
    #Time complexity of push() is O(1)
    def push(self,new_data):
        new_node = Node(new_data)  #allocate
        new_node.next = self.head  # next -> head
        self.head = new_node        # point new to head



    # insert after a given node
    #Time complexity of insertAfter() is O(1) as it does constant amount of work.
    def insertafter(self, prev_node, new_data):
        #check if the give prev_node exists

        if prev_node is None:
            return 

        #create a new node and put in the data
        new_node = Node(new_data)

        #make next of the new node as next of prev node
        new_node.next = prev_node.next
        
        #make next of the new node as next of the prev_node
        prev_node.next = new_node


    # insert at the last
    #Time complexity of append is O(n) where n is the number of nodes in linked list.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        # traverse till the last
        last = self.head
        while(last.next):
            last = last.next
        
        #change the next of last node
        last.next = new_node

    

    #Deletion
        '''
    To delete a node from the linked list, we need to do the following steps. 
    1) Find the previous node of the node to be deleted. 
    2) Change the next of the previous node. 
    3) Free memory for the node to be deleted.

        '''
    
    
    # Given a reference to the head of a list and a key,  
    # delete the first occurence of key in linked list  
    def deleteNode(self, key): 
        prev = None
        #store head node
        temp = self.head

        #if head itself holds key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return 

        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        # if key was not present in the list
        if(temp == None):
            return
        
        # unink the node from inked list
        prev.next = temp.next
        temp = None

    # Given a reference to the head of a list  
    # and a position, delete the node at a given position 
    def deleteNodeatPos(self, position):

        #if link ist is empty
        if self.head == None:
            return
        
        #store head node
        temp = self.head
        
        #if head need to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # find previous node of the node to be selected

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        

        # if pos is more than a number in a node
        if temp is None:
            return
        if temp.next is None:
            return
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next

        # unlink the node from linked list
        temp.next = None

        temp.next = next 
        
    
    # delete link list
    def deletelist(self):
        current = self.head
        while current:
            prev = current.next # move next node
            del current.data
            current = prev

    '''
    # Iterative Solution  (count the link list)

    1) Initialize count as 0 
    2) Initialize a node pointer, current = head.
    3) Do following while current is not NULL
        a) current = current -> next
        b) count++;
    4) Return count 
    '''

    def getCount(self):
        temp = self.head
        count = 0

        while(temp):
            count +=1
            temp = temp.next
        return count

    '''
     Recursive Solution

    int getCount(head)
    1) If head is NULL, return 0.
    2) Else return 1 + getCount(head->next) 
    '''

    def getCountRec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    # searching

    def search(self,li, key):
        '''
        li.search(li.head, key)
        '''
        if not li:
            return false
        
        if li.data == key:
            return True
        return self.search(li.next, key)

    #get nth node
    #Time Complexity: O(n)
    def getNth(self, index):
        count = 0
        current = self.head
        while(current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        # if we get to this line, the caller was asking 
        # for a non-existent element so we assert fail 
        assert (False),"out of index"
        return 0
        

    # revrese list

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev= current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next








if __name__ == '__main__':

    #Start with the empty list
    llist = LinkedList()

    # insert 5
    llist.append(5)

    # insert at the begining
    llist.push(7)

    #insert at the end
    llist.append(9)

    #insert 8 after 7 
    llist.insertafter(llist.head.next, 8)
    
    #delete node
    llist.deleteNode(5)

    llist.printList()
    print(llist.getNth(5))