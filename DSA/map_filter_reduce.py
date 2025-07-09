ls=[1,2,3,4]

cube = lambda x:pow(x,3)
m1=map(cube,ls)
print("printing list after applying map\n",list(m1))

func = lambda x : x>2
f1=filter(func,ls)
print("printing list after applying filter\n",list(f1))

'''
OUTPUT:

printing list after applying map
 [1, 8, 27, 64]
printing list after applying filter
 [3, 4]
'''