
## LeetCode Problem: https://leetcode.com/problems/kth-missing-positive-number/
## Difficulty: Easy 
## Leetcode problem number: 1539

##TC: O(n)
##SC: O(n)

# from typing import List

# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:

#         counter = 1
#         hashmap = {}
#         for num in arr:
#             if num not in hashmap:
#                 hashmap[num] = 1
#             else:
#                 hashmap[num] = hashmap[num] + 1
        
#         while k >0:
#             if counter not in hashmap:
#                 k = k -1
#             counter = counter + 1
#         return counter-1
    

##----------------------------------------------------------------------------

##TC: O(n)
##SC: O(1)

# from typing import List

# class Solution:
#     def findKthPositive(self, a: List[int], k: int) -> int:

#         for i in range(len(a)):
#             if a[i] <= k:
#                 k = k +1
#             else:
#                 break
#         return k


##----------------------------------------------------------------------------

a = [2,3,4,7,11]
k = 5








