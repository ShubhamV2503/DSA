
##LeetCode Problem: Valid Anagram
## Leetcode Problem Number: 242

##TC: O(n log n) due to sorting
##SC: O(n) for storing the sorted strings

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False


###-------------------------------------------------------------------

##Tc: O(n)
##Sc: O(1) since we are using a fixed size array of 26 elements

s = "anagram"
t = "nagaram"

ls = [0]*26

for char in s:
    ls[ord(char)-ord('a')] = ls[ord(char)-ord('a')]  + 1

print(ls)

for char in t:
    ls[ord(char)-ord('a')] = ls[ord(char)-ord('a')]  - 1


for k in ls:
    if k!=0:
        print('false')
    else: 
        print('true')
