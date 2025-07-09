from typing import List

def solve(a:List[List[int]],i,j):
    if i<0 or i>len(a)-1 or j<0 or j>len(a[0])-1 or a[i][j]==0:
        return
    a[i][j]=0
    solve(a,i+1,j)
    solve(a, i - 1, j)
    solve(a, i , j+1)
    solve(a, i , j-1)




def f(a:List[List[int]]):
    n=len(a)
    m=len(a[0])
    ans=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                ans+=1
                solve(a,i,j)
    print(ans)
x=[[0,0],[1,0],[0,1]]
f(x)




