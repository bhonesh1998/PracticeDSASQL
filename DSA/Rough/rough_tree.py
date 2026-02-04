

class Node:

    def __init__(self,key ):
        self.key = key
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0

    l=r=0

    l=height(node.left)
    r=height(node.right)

    return max(l,r)+1

def insert(node,key):
    if node is None:
        return Node(key)
    if node.key < key:
        node.right =  insert(node.right,key)
    else:
        node.left = insert(node.left, key)
    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key)
        inorder(node.right)

root = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)



root = insert(root,1)
root = insert(root,0)
root = insert(root,100)

inorder(root)

print(height(root))








