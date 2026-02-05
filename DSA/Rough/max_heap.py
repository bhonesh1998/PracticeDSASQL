import heapq

def nlargest(number,ls):
    ans = heapq.nsmallest(number,ls)
    ans1 = [-x for x in ans]
    return ans1


ls1 = [1,10,8,7,100]
ls=[-x for x in ls1]

heapq.heapify(ls)


heapq.heappush(ls,-78)

print(-1 * heapq.heappop(ls))


print(-1 * heapq.heappop(ls))


print(nlargest(2,ls))

# print(heapq.nsmallest(2,ls))