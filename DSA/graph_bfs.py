
from collections import deque
from collections import defaultdict
def bfs(g,start,vis,path):
    queue = deque()
    queue.append(start)
    path.append(start)
    vis[start]=True
    while queue:
        x=queue.popleft()
        for n in g[x]:
            if vis[n] == False:
                path.append(n)
                queue.append(n)
                vis[n] = True

    return path


g = defaultdict(list)

v,e = map(int,input().split())

for i in range(e):
    u,v = map(str,input().split())
    g[u].append(v)
    g[v].append(u)

path=[]
vis = defaultdict(bool)
start='A'

print(bfs(g,start,vis,path))

'''

7 9
A B
A C
A F
C E 
C F
C D
D E
D G
G F
['A', 'B', 'C', 'E', 'D', 'G', 'F']

'''






