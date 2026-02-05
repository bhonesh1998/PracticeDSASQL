
'''
insert
inorder
height
level order level wise
search
findmax
findmin
delete
'''

class Node:
    def __init__(self,value):
        self.right=None
        self.left=None
        self.key = value

from collections import defaultdict

def deletenode(node,data):
    if node is None:
        return None
    if node.key<data:
        node.right = deletenode(node.right,data)
    elif node.key>data:
        node.left = deletenode(node.left, data)
    else: # now 4 cases
        if node.left is not None and node.right is not None:
            v=findmax(node.left)
            node.key = v
            node.left = deletenode(node.left,v)
            return node
        elif node.left is not None:
            return node.left
        elif node.right is not None:
            return node.right
        else:
            return None
    return node


def findmin(node):
    if node is None:
        return 0
    ans=10000000
    while(node is not None):
        ans = min(ans,node.key)
        node = node.left
    return ans
def findmax(node):
    if node is None:
        return 0
    ans=-100000
    while(node is not None):
        ans = max(ans,node.key)
        node = node.right
    return ans

def search(node,data):
    if node is None:
        return -1
    if node.key==data:
        return 1
    if node.key < data:
        return search(node.right,data)
    if node.key>data:
        return search(node.left,data)
def level_order(node):
    q=[]
    level=0
    dic=defaultdict(list)
    q.append(node)
    while len(q)>0:
        n=len(q)
        for i in range(n):
            x=q.pop(0)
            dic[level].append(x.key)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        level += 1
    print(dic)
def height(node):
    if node is None:
        return 0
    return max(height(node.left),height(node.right))+1
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key,end=' ')
        inorder(node.right)

def insert(node,data):
    if node is None:
        node=Node(data)
        return node
    if node.key<data:
        node.right = insert(node.right,data)
    else:
        node.left = insert(node.left,data)
    return node

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

print(height(root))

x=1
root = insert(root , x)
print("element inserted ",x)

print(height(root))

x=51
root = insert(root , x)
print("element inserted ",x)

print(height(root))

x=9
root = insert(root , x)
print("element inserted ",x)

print("printing level order wise")
level_order(root)

print(search(root,3))

print(findmax(root))
print(findmin(root))

root  = deletenode(root,1)

inorder(root)
print()

root  = deletenode(root,10)

inorder(root)
print()



root  = deletenode(root,5)
inorder(root)
print()


root  = deletenode(root,9)
inorder(root)
print()


root  = deletenode(root,50)
inorder(root)
print()



