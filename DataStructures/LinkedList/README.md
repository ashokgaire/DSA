
### Array vs Linkist

* An array is the data structure that contains a collection of similar type data elements whereas the Linked list is considered as a non-primitive data structure contains a collection of unordered linked elements known as nodes. 
* In the array the elements belong to indexes, i.e., if you want to get into the fourth element you have to write the variable name with its index or location within the square bracket while in a linked list though, you have to start from the head and work your way through until you get to the fourth element. 
* Accessing an element in an array is fast, while Linked list takes linear time, so it is quite a bit slower. 
* Operations like insertion and deletion in arrays consume a lot of time. On the other hand, the performance of these operations in Linked lists are fast. 
* Arrays are of fixed size. In contrast, Linked lists are dynamic and flexible and can expand and contract its size. 
*. In an array, memory is assigned during compile time while in a Linked list it is allocated during execution or runtime. 
* Elements are stored consecutively in arrays whereas it is stored randomly in Linked lists. 
* The requirement of memory is less due to actual data being stored within the index in the array. As against, there is a need for more memory in Linked Lists due to storage of additional next and previous referencing elements. 
* In addition memory utilization is inefficient in the array. Conversely, memory utilization is efficient in the linked list. 


#Following are the points in favour of Linked Lists. 


* The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage, and in practical uses, the upper limit is rarely reached. 

* Inserting a new element in an array of elements is expensive because a room has to be created for the new elements and to create room existing elements have to be shifted. 

For example, suppose we maintain a sorted list of IDs in an array id[ ]. 

id[ ] = [1000, 1010, 1050, 2000, 2040, …..]. 

And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000). 

Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved. 

So Linked list provides the following two advantages over arrays 
1) Dynamic size 
2) Ease of insertion/deletion 

Linked lists have following drawbacks: 
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists. 
2) Extra memory space for a pointer is required with each element of the list. 
3) Arrays have better cache locality that can make a pretty big difference in performance.



#reference
https://www.geeksforgeeks.org/linked-list-vs-array/