
## LeetCode Problem: Best Time to Buy and Sell Stock
## Leetcode problem number: 121

## TC: O(n^2)
## SC: O(1)

# from typing import List
# class Solution:
#     def maxProfit(self, a: List[int]) -> int:

#         start = 0
#         if len(a) >1:
#             start = 1
#         mini = float('inf')
#         sell = 0
#         maxi = float('-inf')
#         for i in range(start,len(a)):
#             sell = a[i]
#             for j in range(i+1):
#                 if a[j] < sell:
#                     maxi = max(maxi , sell - a[j])
#         if maxi >0:
#             return maxi
#         else:
#             return 0
        

###----------------------------------------------------------

## TC: O(n)
## SC: O(1)

from typing import List
class Solution:
    def maxProfit(self, a: List[int]) -> int:

        minimum = a[0]
        current = 0
        maximum_profit = 0
        if len(a)>1:
            for i in range(1,len(a)):
                current = a[i] - minimum
                maximum_profit = max(maximum_profit,current)
                minimum = min(minimum,a[i])
        return(maximum_profit)




