

input_ls = [3,10,30,-2,100,10000]

# [6,20,60,-4,200,20000]

# f(f(x)) , f(g(x)) fog gof

output_object =map(lambda x:x**2, input_ls)

print(output_object)

for x in output_object:
    print(x)

output_list = list(map(lambda x:x**3, input_ls))

print(output_list)




