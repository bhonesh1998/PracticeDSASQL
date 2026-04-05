

sq = []

for i in range(10): # 0,2,4,6,8
    if i%2==0:
        sq.append(i**2)

print(sq)


sq = [x**2 for x in range(10) if x%2==0]
print(sq)

ex1 = [i*3 for i in range(5)]
print(ex1)
print(type(ex1))
# even

ex2 = [i+10 for i in range(5) ]
print(ex2)