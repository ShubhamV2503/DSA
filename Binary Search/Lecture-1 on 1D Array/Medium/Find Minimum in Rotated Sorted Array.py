
## LeetCode 153: Find Minimum in Rotated Sorted Array
## TC: O(log n)
## SC: O(1)


a = [4,5,6,7,10,1,2,3]

start = 0
end = len(a)-1
mini = float('inf')

while start<=end:
    mid = (start+end)//2
    if a[start] <= a[mid]:
        mini = min(mini,a[start])
        start = mid + 1
    else:
        mini = min(mini,a[mid])
        end = mid -1
print(mini)