'''


The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
'''



import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i])