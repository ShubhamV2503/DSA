
##LeetCode Problem: Majority Element II
##Leetcode Problem Number: 229

##TC: O(n)
##SC: O(n)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for key in nums:
            if key not in hashmap:
                hashmap[key] = 1
            else:
                hashmap[key] = hashmap[key] + 1
        
        ans = []
        for k in hashmap:
            if hashmap[k] >len(nums)/3:
                ans.append(k)
        return ans
    
