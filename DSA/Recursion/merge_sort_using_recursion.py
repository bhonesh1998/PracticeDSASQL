
def merge(a,low,mid,high):
    arr=[]
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if a[left]<=a[right]:
            arr.append(a[left])
            left +=1
        else:
            arr.append(a[right])
            right+=1
    while left<=mid:
        arr.append(a[left])
        left+=1
    while right<=high:
        arr.append(a[right])
        right += 1
    for i in range(low,high+1):
        a[i]=arr[i-low]


def mergesf(a,low,high):

    if low>=high:
        return
    mid = (low + high) // 2

    mergesf(a,low,mid)
    mergesf(a, mid+1, high)
    merge(a,low,mid,high)

a=[10,4,0,9]
mergesf(a,0,3)
print(a)


'''
TC - NLOGN
'''