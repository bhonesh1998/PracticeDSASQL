import heapq

ls = [1,10,8,7,100]

heapq.heapify(ls)

print(ls)

heapq.heappush(ls,78)

print(ls)

print(heapq.heappop(ls))

print(ls)

print(heapq.heappop(ls))

print(ls)

heapq.heappushpop(ls,1)

print(ls)

print(heapq.nlargest(2,ls))

print(heapq.nsmallest(2,ls))