
## LeetCode Problem: Rotate String
## Leetcode Problem Number: 796

##TC: O(n^2)
##SC: O(n)

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         start = 0
#         bool = False
#         for i in range(len(s)):
#             bool = False
#             if s[i] == goal[0]:
#                 start = i
#             temp = start

#             st = ''
#             counter = 0
#             while start != len(s):
#                 st = st + s[start]
#                 start = start +1

#             while counter != temp:
#                 st = st + s[counter]
#                 counter = counter +1

#             if st == goal:
#                 bool = True
#                 break


#         if bool is True:
#             return True
#         return False


##------------------------------------------------------------

##Tc: O(n)
##SC: O(n)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            s = s + s
            if goal in s:
                return True
        return False
    
