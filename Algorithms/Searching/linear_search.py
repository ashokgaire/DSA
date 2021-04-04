'''

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1

time compexity o(n)
'''

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)