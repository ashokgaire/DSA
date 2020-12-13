#!/usr/bin/python3

'''An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. 
This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., 
the memory location of the first element of the array (generally denoted by the name of the array).

array(data type, value list)



Type Code 	C Type 	                   Python Type 	                                         Minimum size in Bytes
‘b’ 	signed char                      	    int 	                                              1
‘B’ 	unsigned char 	                        int 	                                              1
‘u’ 	Py_UNICODE 	                      unicode character                                           2
‘h’ 	signed short 	                        int 	                                              2
‘H’ 	unsigned short 	                        int 	                                              2
‘i’ 	signed    int 	                        int 	                                              2
‘I’ 	unsigned   int 	                        int 	                                              2
‘l’ 	signed long 	                        int 	                                              4
‘L’ 	unsigned long 	                        int 	                                              4
‘q’ 	signed long long 	                     int 	                                              8
‘Q’ 	unsigned long long 	                     int 	                                              8
‘f’ 	float 	                                  float 	                                          4
‘d’ 	double 	                                float 	                                              8







2. append():- This function is used to add the value mentioned in its arguments at the end of the array.
3. insert(i,x) :- This function is used to add the value(x) at the ith position specified in its argument.
4. pop():- This function removes the element at the position mentioned in its argument and returns it.
5. remove():- This function is used to remove the first occurrence of the value mentioned in its arguments.
 6.index() :- This function returns the index of the first occurrence of value mentioned in arguments.
7. reverse() :- This function reverses the array.
 
'''



import array

arr = array.array('i',[1,2,3])

#print
print("created array is : ")
for i in range(0,len(arr)):
    print(arr[i])


# append vaes at the end
arr.append(4)

# insert 
arr.insert(2,5)

#print
print("new array is : ")
for i in range(0,len(arr)):
    print(arr[i])


#pop
arr.pop(1)

#remove
arr.remove(5)


#print
print("new array is : ")
for i in range(0,len(arr)):
    print(arr[i])



#index
print(f"index of 1 {arr.index(1)}")


#reverse
arr.reverse()

#print
print("new array is : ", end = "")
for i in range(0,len(arr)):
    print(arr[i])