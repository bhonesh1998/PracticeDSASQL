
ss='hello'
ans=[0]*len(ss)
sh = 3
for i in range(len(ss)):
    iv = ord(ss[i])
    ans[i]= chr((iv+(sh)%26))
print(ans)


print(2+3,2-3,2*3,2/3)

print(2**3)

print(5//2,5/2)

print(17%3)

print(3*"a"+"b")

print("don't") # double quotes here

print('don\'t') # escape seq single quotes here

print('py' 'thon') # auto concat but dont concat variable and literal

x='py'
print(x+'thon') # use + to add lit and variable

word = 'Bhonesh'

print(word.index('h'))

print("count of h letter"+str(word.count("h")))

# find , upper , startswith  method
# str.find
# str.upper
# str.startswith
# str.swapcase upper ko lower and lower ko upper
# replace and split
# "$"join(str) -> join string with delimiter
# title method
# str[::-1] to reverse
# str[::7] every 7th letter



print(word[0],word[4],word[6])

print(word[-1]) # last character

print(word[0:2]) # slicing , last index excluded , 2 letters will be printed

print(word[2:]) # slice from 2 upto end

print(word[:5]) # slice from start upto 4

# word[0]='x' # strings are immutable - will give error










