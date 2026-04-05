
# sum of maximum element in each row

# 3 + 6 + 9 + 10 -> 28


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,10]
]

print(matrix)

n = len(matrix)

answer = 0

for i in range(n):
    mx_row = -1
    for j in range(len(matrix[i])): #
        mx_row = max(mx_row,matrix[i][j])
    answer+=mx_row
print(answer)

ans=0
for i in range(n):
    ans+=max(matrix[i])
print(ans)


