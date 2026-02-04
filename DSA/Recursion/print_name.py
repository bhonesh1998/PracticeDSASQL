def f(i,n):
    if i>n:
        return
    print("bhonesh",i)
    return f(i+1,n)
f(1,3)

'''
TC O(N)
SC O(N) internal memory of computer
'''