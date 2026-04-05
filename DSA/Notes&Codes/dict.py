
dic = {}

a_list = [1,2,3,4] # keys

b_list = [10,20,30,40] # values

n= len(a_list)

for i in range(n):
    dic[a_list[i]]=b_list[i]

print(dic)

print(dic[3])

for k,v in dic.items():
    print(k,v)

print(dic.keys())
print(dic.values())

dic[3]=60

print(dic)

del dic[3]

print(dic)

dic.pop(1)

print(dic)

dic[5]=200

print(dic)

print(dic.get(5))

d = dict()

d[1]=2

print(d)