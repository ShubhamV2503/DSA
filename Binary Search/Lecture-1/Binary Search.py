
## LeetCode 704: Binary Search
## LeetCode Problem Link: https://leetcode.com/problems/binary-search/

##TC: O(n)
##SC: O(1)

# from typing import List

# class Solution:
    
    #   nums = [-1,0,3,5,9,12], target = 9
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1


##---------------------------------------------------------------------

## TC: O(log n)
## SC: O(1)
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)// 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return -1