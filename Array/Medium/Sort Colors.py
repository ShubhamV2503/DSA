
## Leetcode 75. Sort Colors
## https://leetcode.com/problems/sort-colors/
## Leetcode problem number: 75

##TC: O(n)+O(n/2)+O(n/2) = O(n)
##SC: O(1)

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        for i in range(cnt0):
            nums[i] = 0

        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2


###----------------------------------------------------------








