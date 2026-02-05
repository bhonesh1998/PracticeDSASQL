


# lambda function

ls=[[1,3],[2,6],[8,10],[15,18]]
# ls=[[1,2],[4,5],[1,3]]
ls.sort(key=lambda x:x[0])
print(ls)

n=len(ls)
i=0
ls1=[]
for i in range(n-1):
    if ls[i][1]>=ls[i+1][0]:
        ls1.append([ls[i][0],ls[i+1][1]])
    else:
        ls1.append(ls[i+1])
print(ls1)

# ls = ["a b","c a"]
# ls.sort()
# print(ls)
#
# ls.sort(key=lambda x:x.split()[1])
# print(ls)

