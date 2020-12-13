### Binary Search Tree 
is a node-based binary tree data structure which has the following properties:

    * The left subtree of a node contains only nodes with keys lesser than the node’s key.
    * The right subtree of a node contains only nodes with keys greater than the node’s key.
   *  The left and right subtree each must also be a binary search tree.

## Insertion: 
1. Start from the root. 
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right. 
3. After reaching the end, just insert that node at left(if less than current) else right. 


### Time Complexity: 
The worst-case time complexity of search and insert operations is O(h) where h is the height of the Binary Search Tree. In the worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n). 