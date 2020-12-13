'''
1. Data
2. Pointer to left child
3. Pointer to right child

'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# inorder traversa of a binary tree
def inorder(temp):
    if(not temp):
        return 
    inorder(temp.left)
    print(temp.key, end= " ")
    inorder(temp.right)

# insertion
def insert(temp, key):
    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)

    # do level order traversal until we find an empty place
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        
        if not temp.right:
            temp.right = Node(key)
            break 
        
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(11) 
    root.left.left = newNode(7) 
    root.right = newNode(9) 
    root.right.left = newNode(15) 
    root.right.right = newNode(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
