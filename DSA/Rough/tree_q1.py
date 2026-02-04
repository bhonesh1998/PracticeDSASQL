class Node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.key=value

def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left)+count_leaf_nodes(node.right)


def insert(node,value):
    if node is None:
        node = Node(value)
    elif node.key<=value:
        node.right=insert(node.right,value)
    elif node.key>value:
        node.left = insert(node.left,value)
    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key,end=' ')
        inorder(node.right)
root=None
l = list(map(int,input().split()))
for i in range(len(l)):
    root=insert(root,l[i])
inorder(root)
print(count_leaf_nodes(root))