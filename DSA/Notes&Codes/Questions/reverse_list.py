'''

input_ls = [2,3,4,5,10,90]

reverse the input_ls

in-place reverse

no another list is allowed

input ls 1. read
2. logic
3. input ls

'''



input_ls = [2,3,4,5,10,90]
c=0
for x in input_ls:
    c+=1
n=c
for i in range(n//2):
    input_ls[i],input_ls[n-i-1] = input_ls[n-i-1],input_ls[i]
print(input_ls)











