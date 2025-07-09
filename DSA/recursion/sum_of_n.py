def f(i,sum,steps):
    if i<1:
        return sum
    print("step",steps,sum)
    return f(i-1,sum+i,steps+1)


x=f(5,0,0)
print(x)