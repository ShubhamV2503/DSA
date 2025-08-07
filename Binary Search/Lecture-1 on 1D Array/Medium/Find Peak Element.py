
## LeetCode 162: Find Peak Element
## leetcode https://leetcode.com/problems/find-peak-element/
## TC: O(n)
## SC: O(1)


# nums = [1,2,1,3,5,6,4]

# prev = 0
# current = 1
# maxi = 0

# for i in range(len(nums)-1):
#     if nums[prev] < nums[current]:
#         maxi = max(maxi,current)
#         prev = prev +1
#         current = current + 1
#     else:
#         prev = prev + 1
#         current = current + 1
# print(maxi)

##---------------------------------------------------------------------------

##TC: O(N)
##SC: O(1)

# from typing import List

# class Solution:
#     def findPeakElement(self, a: List[int]) -> int:

#         if len(a) > 1:
#             for i in range(len(a)):
#                 if i == 0:
#                     if a[i] > float('-inf') and a[i] > a[i+1]:
#                         return(i)
#                 elif i == len(a)-1:
#                     if a[i] > float('-inf') and a[i] > a[i-1]:
#                         return(i)
#                 else:
#                     if a[i] > a[i+1] and a[i] > a[i-1]:
#                         return(i)
#         return 0


##---------------------------------------------------------------------------

##TC: O(logN)
##SC: O(1)

from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:

        start = 0
        end = len(a)-1
        if len(a)>1:
            if  a[0] > a[1]:
                return start
            if  a[end] > a[end-1]:
                return end
            start = 1
            end = end-1
            while start <= end:
                mid = (start+end)//2
                if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                    return mid
                if a[mid] > a[mid-1]:
                    start = mid+1
                else:
                    end = mid-1 
        return 0



