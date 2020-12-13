'''
1. Data
2. Pointer to left child
3. Pointer to right child

'''

class newNode:
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
        root = newNode(key)
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
            temp.right = newNode(key)
            break 
        
        else:
            q.append(temp.right)

# function to delete the given deepest node (d_node) in binary tree  
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.data 
        deleteDeepest(root,temp) 
        key_node.data = x 
    return root 
   

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
