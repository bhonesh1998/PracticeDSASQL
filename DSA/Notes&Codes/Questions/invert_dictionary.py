# invert dictionary
# k<>v
# v<>k
# output -> vishal a , ram b , sita c

input_dict = {
    'a':'vishal',
    'b':'ram',
    'c':'sita'
}

output_dict = {}

for k,v in input_dict.items():
    output_dict[v]=k

print(output_dict)



