##LeetCode Problem: Largest Odd Number in String
## Leetcode Problem Number: 1903

# Time Complexity: O(n²)
# Space Complexity: O(n)

# class Solution:
#     def largestOddNumber(self, num: str) -> str:
        
#         stored = ''
#         bool = False
#         for i in range(len(num) - 1, -1, -1) :
#             if num[i] in {'1','3','5','7','9'} :
#                 bool = True
#                 break
#         if bool is True:
#             for k in range(0,i+1):
#                 stored = stored + num[k]
#             return stored
#         return ''


###-----------------------------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)


# class Solution:
#     def largestOddNumber(self, num: str) -> str:
#         for i in range(len(num) - 1, -1, -1):
#             if num[i] in {'1', '3', '5', '7', '9'}:
#                 return num[:i+1]
#         return ''

