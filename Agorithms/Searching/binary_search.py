'''
Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty


Compare x with the middle element.
If x matches with middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
Else (x is smaller) recur for the left half.

'''

## Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):

    # check base case
    if r >= l:
        mid =  l + (r - l) // 2   # divide from half

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr,l, mid-1,x)

        else:
            return binarySearch(arr, mid +1 , r ,x)
    else:
        return -1




# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
