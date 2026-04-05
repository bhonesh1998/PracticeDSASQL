

# create sets

number_set = {1,2,3,1,3,4,5,5,10,10,10}

print(number_set)

#list to set

fruit_list = ["apple","orange","kiwi","apple","pineapple","kiwi"]

fruit_set = set(fruit_list)

print(fruit_set)

# set()

set_1 = set()

set_1.add(2)

# add()
set_1.add(3)

set_1.add(5)

print(set_1)

set_1.add(5)

print(set_1)


# remove()

set_1.remove(5)

print(set_1)

# discard

set_1.discard(2)

print(set_1)

set_1.add(10)

set_1.add(11)

set_1.add(12)

print(set_1) # 3,10,11,12

# remove vs discard

set_1.discard(12)

print(set_1)


# set_1.discard(12)

ls = [1,2,100,200]

set_1.update(ls)

print(set_1)


#############################################################################

set_a = {1,2,3}

set_b = {4,5,6,3,2}

set_union = set_a.union(set_b)

print(set_a)
print(set_b)
print(set_union)

set_intersection = set_a.intersection(set_b)

print(set_intersection)

set_minus = set_a.difference(set_b) # item is there in set a but not in set b

set_minus_2 = set_b.difference(set_a) # item is there in set b but not in set a

print(set_minus_2)













