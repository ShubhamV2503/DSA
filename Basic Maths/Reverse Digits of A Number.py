# This is LeetCode problem 7
## Mine code

class Solution(object):
    def reverse(self, x):
        MIN_INTEGER = -2**31
        MAX_INTEGER =  2**31 - 1
        res = 0
        rev = 0
        flag = 0
        if x < 0:
            x = 0 - x
            flag = 1
        while (x>0):
            rem = x % 10
            x = x // 10
            rev = rev *10 + rem
        if flag == 1:
            rev = 0  - rev
        res = rev

        if res >= MAX_INTEGER or res <= MIN_INTEGER:
            return 0
        return res
        

# Time Complexity: O(Log n)
# Space Complexity : O(1)                     
#-------------------------------------------------------------------------------#


