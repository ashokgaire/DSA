import math

def jumpSearch(arr, x, n):
    #finding bock size to be jumped
    step= math.sqrt(n)

    #finding the block where eement is present
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step +=math.sqrt(n)
        if prev >=n:
            return -1

    # doing a linear search for x in bock begining with prev
    while arr[int(prev)] < x:
        prev +=1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev
    return -1


# Driver code to test function
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# Find the index of 'x' using Jump Search
index = jumpSearch(arr, x, n)

# Print the index where 'x' is located
print("Number", x, "is at index", "%.0f" % index)