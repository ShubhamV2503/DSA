
## LeetCode Problem: https://leetcode.com/problems/single-number/
## LeetCode Problem Number: 136

## TC: O(n)
## SC: O(1)


class Solution:
    def singleNumber(self, nums):

        xor = 0

        for k in nums:
            xor = xor^k
        return xor
        