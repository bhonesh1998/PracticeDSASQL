

'''


sorted ( list , key = some lambda function , reverse = False)


reverse can be changed to True , by default it is False


'''


ls = [2,4,5,6,0,10,100]

ls1=sorted(ls)

print(ls1)


ls2=sorted(ls,reverse=True)

print(ls2)


ls3=sorted(ls, key = lambda x : -1*x )

print(ls3)