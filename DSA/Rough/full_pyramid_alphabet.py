
def full_pyramid(n):

    for i in range(1,n+1):
        alpha = 65
        for j in range(n-i):
            print(" ",end="")
        for k in range(1,i+1):
            print(chr(alpha)+" ",end="")
            alpha+=1
        print("\n")

full_pyramid(5)