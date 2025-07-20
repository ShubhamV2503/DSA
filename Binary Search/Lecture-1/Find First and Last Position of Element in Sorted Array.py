## LeetCode Problem: Find First and Last Position of Element in Sorted Array
## Leetcode Proble number: 34

##TC: O(n)
##SC: O(1)

# from typing import List

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         res = []
#         for i in range(len(nums)):
#             if target == nums[i]:
#                 res.append(i)
        
#         if len(res) == 1:
#             res.append(res[0])

#         if len(res) > 0:
#             return [res[0] , res[len(res)-1]]
#         return [-1,-1]

##----------------------------------------------------------------------------------

a = [3,4,13,13,13,20,40 ]
nums = [5,7,7,8,8,10]
target = 11

start = 0
end = len(nums)
res = len(nums)-1

while start <= end:
    mid = (start+end) // 2
    if a[mid] >=x :
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)




