
##LeetCode Problem: Longest Common Prefix
##Leetcode problem number: 14

##TC: O(n*m) where n is the number of strings and m is the length of the shortest string
##SC: O(1) as we are not using any extra space

# st = ["flower","flow","flight"]

# minimum_length = float('inf')

# for temp in st:
#     if len(temp) < minimum_length:
#         minimum_length = len(temp)

# counter = 0
# while counter != minimum_length:
#     for temp in st:
#         if temp[counter] != st[0][counter]:
#             print(st[0][:counter])
#             break
#     counter  = counter +1
# print(st[0][:counter])


##--------------------------------------------------

##TC: O(n log n + m)
##SC: O(1) as we are not using any extra space

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()  # Sort lexicographically
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]

