
list1 = [1,10,20,30,100,-9,-100]

list2 = sorted(list1)

print(list1)
print("after sorting")
print(list2)

list3 = sorted(list1, reverse=True)

# sorting -> desc to asc number

print(list3)

list_fruit = ["apple","kiwi","fig","pomegranate"]

print(sorted(list_fruit))
print(sorted(list_fruit,key=len,reverse=False))
print(sorted(list_fruit,key=len,reverse=True))

# tuple - first name ,  second score

# ('Aman',85) -> x[0]=Aman , x[1]=85

scorecard = [ ('Aman',85) , ('Sana',60) , ('Ram',90) , ('Venkatesh',78)]

answer = sorted(scorecard,key=lambda x:x[1],reverse=True)

print(answer)


scorecard = [ ('Aman',85,30) , ('Sana',90,40) , ('Ram',90,20) , ('Venkatesh',78,0)]

answer = sorted(scorecard,key=lambda x:x[2]+x[1],reverse=False)

print(answer)




