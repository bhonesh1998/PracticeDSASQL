maze = [
[1, 0, 0, 0],
[1, 1, 1, 0],
[0, 1, 0, 0],
[0, 1, 1, 1]
]

def issafe(x,y,r,c):
    if x<r and y<c:
        return True
    else:
        return False
def run(a,x,y):
    if a[x][y]==1:
        return True
    else:
        return False


r=len(maze)
c=len(maze[0])
ans=[]
path=[]

def backtrack(x,y):
    if x==r-1 and y==c-1:
        ans.append(path.copy())
        return

    print(path)

    path.append((x,y))

    print(path)

    if issafe(x,y+1,r,c) and run(maze,x,y+1):
        backtrack(x,y+1)
    if issafe(x+1,y,r,c) and run(maze,x+1,y):
        backtrack(x+1,y)

    x=path.pop()
    print("popped ",x)


if run(maze,0,0):
    backtrack(0,0)

print(ans)







