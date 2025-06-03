## This is LeetCode problem 9
# https://leetcode.com/problems/palindrome-number/

# Mine code

class Solution(object):
    def isPalindrome(self, x):

        copy = x
        rev = 0
        if x < 0:
            return False
        else:
            while x > 0:
                rem = x % 10
                x = x // 10
                rev = rev * 10 + rem

            if rev == copy:
                return True
            return False



# Time Complexity: O(N)
# Space Complexity : O(1) 