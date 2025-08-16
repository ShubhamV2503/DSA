
##Leetcode Problem: Rotate Image by 90 degrees clockwise
## leet code problem number 48

##Tc: O(n^2)
##Sc: O(n*n)

# import numpy as np
# # a = [[1, 2, 3,4], [5,6,7,8], [9, 10, 11,12],[13,14,15,16]]
# a = [[1,2,3],[4,5,6],[7,8,9]]
# n = len(a)
# ans = [[0] * n for _ in range(n)]
# print(ans)

# print(a)

# temp = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         ans[j][n-1-i] = a[i][j]
# print(ans)

##------------------------------------------------------------------

##Tc: O(n^2)
##Sc: O(1)

from typing import List
class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        a = [[1, 2, 3,4], [5,6,7,8], [9, 10, 11,12],[13,14,15,16]]
        temp = 0
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i][j] != a[j][i] and i < j:
                    temp = a[i][j]
                    a[i][j] = a[j][i]
                    a[j][i] = temp
        
        for i in range(len(a)):
            a[i].reverse()










