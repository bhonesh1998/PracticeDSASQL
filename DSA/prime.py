# import math
#
# def solve(x,c):
#     if x == 0 or x == 1:
#         return x
#     else:
#         while x > 0:
#             if p(x):
#                 x -= 1
#                 c += 1
#             else:
#                 x = pp(x)
#                 c += 1
#         return c
# def pp(n):
#     a=0
#     b=0
#     mi=-100
#     for i in range(2,n):
#         if n%i==0:
#             if mi<abs((i-(n//i))):
#                 a=i
#                 b=n//i
#                 mi=abs((i-(n//i)))
#     print(a,b)
#     return max(a,b)
#
#
# def p(n):
#     if n==2 or n==3:
#         return 1
#     else:
#         for i in range(2,int(math.sqrt(n)+1)):
#             if n%i==0:
#                 return 0
#     return 1
#
# x=int(input())
# c=0
# print(solve(x,c))


# 966514

# import math
# def solve_dp(n):
#     dp=[0]*(1000000+1)
#     if n==0 or n==1 or n==2 or n==3:
#         dp[n]=n
#     else:
#
#         for i in range(2,int(math.sqrt(n))+1):
#             if n%i==0:
#                 dp[i]=min(dp[i],dp[n//i]+1)
#     return dp[n]
#
#
# print(solve_dp(4))


def sieve_of_eratosthenes(n):

    primes = [True] * (n + 1)

    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):

        if primes[i]:

            for j in range(i * i, n + 1, i):

                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]



def max_prime_factor_dp(n):

    dp = [0] * (n + 1)

    primes = sieve_of_eratosthenes(n)

    for i in range(2, n + 1):

        if dp[i] == 0:

            for prime in primes:

                if i % prime == 0:

                    dp[i] = prime

                    break

    return dp[n]

print(max_prime_factor_dp(966514))