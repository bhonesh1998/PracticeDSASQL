class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:

        a = sorted(a)
        i = 0
        n = len(a)
        s = []
        for i in range(n):
            if (i > 0 and a[i] == a[i - 1]):
                continue
            j = i + 1
            k = n - 1
            while j < k:
                # print(i,j,k,x)
                x = a[i] + a[j] + a[k]
                if x == 0:
                    s.append([a[i], a[j], a[k]])
                    j += 1
                    k -= 1
                    while (j < k and a[j] == a[j - 1]):
                        j += 1
                    while (j < k and a[k] == a[k + 1]):
                        k -= 1
                elif x > 0:
                    k -= 1
                else:
                    j += 1
            # i+=1
        return s


