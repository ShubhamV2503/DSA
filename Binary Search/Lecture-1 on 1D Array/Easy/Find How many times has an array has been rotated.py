


a = [4,5,6,7,0,1,2,3]

start = 0
end = len(a)-1
mini = float('inf')
index = -1
while start<=end:
    mid = (start+end)//2
    if a[start] <= a[mid]:
        # mini = min(mini,a[start])
        if a[start] <= mini:
            index = start
            mini = a[start]
        start = mid + 1
    else:
        # mini = min(mini,a[mid])
        if a[mid] <= mini:
            mini = a[mid]
            index = mid
        end = mid -1
print(mini)
print(index)

