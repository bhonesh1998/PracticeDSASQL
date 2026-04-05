

from functools import reduce

input_list = [1,2,3,4,5]

output_value = reduce(lambda x,y : x+y , input_list)

print(output_value)


input_list_2 = [1,2,3,4,5]
output_value_2 = reduce(lambda x,y : max(x,y) , input_list_2)
print(output_value_2)


'''

input_list = [1,2,3,4,5]
lambda x,y : x+y 

1+2 -> 3

3+3 -> 6

6 + 4 -> 10

10 + 5 -> 15

'''


