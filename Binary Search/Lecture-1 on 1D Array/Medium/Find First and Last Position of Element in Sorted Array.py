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

##TC: O(log n)
##SC: O(1)

from typing import List

class Solution:
    def searchRange(self, a: List[int], x: int) -> List[int]:

        def lowerbound(a,x):
            start = 0
            end = len(a)-1
            res = len(a)

            while start <= end:
                mid = (start+end) // 2
                if a[mid] >=x:
                    res = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return(res)

        def upperbound(a,x):
            start = 0
            end = len(a)-1
            res = len(a)

            while start <= end:
                mid = (start+end) // 2
                if a[mid] >x :
                    res = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return(res)
        ans = lowerbound(a,x)
        print(ans,len(a))
        if ans == len(a)or a[ans] != x:
            return [-1,-1]
        return [ans, (upperbound(a,x))-1]

