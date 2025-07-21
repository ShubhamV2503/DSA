## Leetcode #33. Search in Rotated Sorted Array
## Tc: O(n)
## Sc: O(1)


# from typing import List
# class Solution:
#     def search(self, a: List[int], target: int) -> int:
#         for i in range(len(a)):
#             if a[i] == target:
#                 return i
#         return -1


##--------------------------------------------------------------

a = [7,8,9,1,2,3,4,5,6]

start = 0
end = len(a)-1
res = -1
target = 8

while start<=end:
    mid = (start+end)//2
    if a[mid] == target:
        res = (mid)
        break
    if a[start] <= a[mid]:
        if a[start]<=target and target <= a[mid]:
            end = mid - 1
        else:
            start = mid+1
    else:
        if a[mid] <= target and target <= a[end]:
            start = mid+1
        else:
            end = mid - 1

print(res)