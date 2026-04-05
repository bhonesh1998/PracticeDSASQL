

# map and filter
# one to one
# higher order function (function as input )
# [2,10,100,5,8,7,6,5,3]
# 2%2 == 0 -> true -> 2


input_list = [2,10,100,5,8,7,6,5,3]

# filter out odd even numbers

even_list = list(filter(lambda x : x%2 == 0 , input_list )) # even numbers

odd_list = list(filter(lambda x : x%2 == 1 , input_list )) # odd numbers

print(odd_list)

