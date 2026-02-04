
'''

l.append(element)
l.remove(element)
l.pop(index)
l.index(element)
l.insert(index,element)
l.extend(list2)
l.count(element) -> occurrence of element
sorted(ls)
sorted(my_list,reverse=True) # desc
min(l)
max(l)
sum(l)
l.clear() remove all elements
zip(ls1,ls2) iterate through multiple lists
"pen" in ["x","y","pen"]

'''



ls = [1,2,3]

print(ls)

# list is mutable
# direct assignment will refer same address

ls1 = ls
ls1.append(5)
print(ls)

# shallow copy - no change in original list

ls2 = ls[:]
ls2.append(7)
print(ls)

ls = [2,4,5,10]
print(ls)

ls.remove(4)
print(ls)

ls.pop(0)
print(ls)
