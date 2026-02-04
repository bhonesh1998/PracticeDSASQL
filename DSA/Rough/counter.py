

# >>> sorted(counter.items())


from collections import Counter
ls = [2,2,2,1,1,5,5,0,9]
c=Counter(ls)
print(c)
ls = list(c.keys())
fre = list(c.values())
for ele , freq in zip(ls,fre):
    print('element {} is having freq {}'.format(ele,freq))

'''
OUTPUT :

Counter({2: 3, 1: 2, 5: 2, 0: 1, 9: 1})
element 2 is having freq 3
element 1 is having freq 2
element 5 is having freq 2
element 0 is having freq 1
element 9 is having freq 1
'''