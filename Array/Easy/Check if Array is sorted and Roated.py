

##LeetCode Problem: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
## leetcode Problem Number: 1752
## Time Complexity: O(n)
## Space Complexity: O(1)

from typing import List

class Solution:
    def check(self, a: List[int]) -> bool:

        if a[len(a)-1] > a[0]:
            count = 1
        else:
            count = 0

        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                count = count + 1
            
            if count > 1:
                return False
        return True