
'''
insert
traversal
height
search
search level wise


'''

class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left),height(node.right))+1



def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key)
        inorder(node.right)

def insert(node , key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left , key)
    else:
        node.right = insert(node.right , key)
    return node

def search(node,data):

    if node.key==data:
        print("data found ",node.key)
        if node.left:
            print("left child is -> ",node.left.key)
        if node.right:
            print("right child is -> ",node.right.key)

        return
    elif node.key < data:
        if node.right:
            return search(node.right,data)
    else:
        if node.left:
            return search(node.left, data)

def search2(node,data,level):

    if node.key==data:
        print("data found at level",level)
        if node.left:
            print("left child is -> ",node.left.key)
        if node.right:
            print("right child is -> ",node.right.key)

        return
    elif node.key < data:
        if node.right:
            return search2(node.right,data,level+1)
    else:
        if node.left:
            return search2(node.left, data,level+1)


root = None

x=10

root = insert(root , x)
print("element inserted ",x )

x=50
root = insert(root , x)
print("element inserted ",x)

x=5
root = insert(root , x)
print("element inserted ",x)


print("printing inorder traversal")

inorder(root)
x=1000
root = insert(root , x)
print("element inserted ",x)

print("printing inorder traversal")
inorder(root)

x=1
root = insert(root , x)
print("element inserted ",x)

x=6
root = insert(root , x)
print("element inserted ",x)
print("printing inorder traversal")

x=0
root = insert(root , x)
print("element inserted ",x)


inorder(root)

search(root,6)
search2(root,6,0)
search2(root,0,0)

print(height(root))


def printTree(root, space=0, level_space=5):
    if root is None:
        return

    # Increase distance between levels
    space += level_space

    # Process right child first
    printTree(root.right, space)

    # Print current node after space count
    print()
    print(' ' * (space - level_space) + str(root.key))

    # Process left child
    printTree(root.left, space)

printTree(root,0,5)





