

## LeetCode Problem: https://leetcode.com/problems/max-consecutive-ones/
## Leetcode Problem Number: 485

## TC: O(n)
## SC: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0

        for k in nums:
            if k == 1:
                counter = counter +1
            else:
                if counter > max:
                    max = counter
                counter = 0
        if counter > max:
            return counter
        else:
            return max
        

