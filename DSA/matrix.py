

r = int(input("enter number of rows"))
c = int(input("enter number of columns"))

ar=[]

for i in range(r):

    col=[]

    for j in range(c):
        x=int(input())
        col.append(x)
    ar.append(col)

for i in range(len(ar)):
    for j in range(len(ar[i])):
        print(ar[i][j],end=' ')
    print('')

print(ar)