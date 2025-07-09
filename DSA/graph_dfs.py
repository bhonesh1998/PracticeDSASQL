

def dfs(g,start,vis,path):
    path.append(start)
    vis[start]=True
    for n in g[start]:
        if vis[n]==False:
            dfs(g,n,vis,path)

    return path


from collections import defaultdict

g = defaultdict(list)

v,e = map(int,input().split())

for i in range(e):
    u,v = map(str,input().split())
    g[u].append(v)
    g[v].append(u)

path=[]
vis = defaultdict(bool)
start='A'

x=dfs(g,start,vis,path)
print(x)


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






