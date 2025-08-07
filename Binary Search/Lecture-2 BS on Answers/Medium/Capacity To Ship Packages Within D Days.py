
## LeetCode Problem: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
## Leetcode Problem Number: 1011
##TC: O(N * (sum(a[]) - max(a[]) + 1)) ~ O(N*N)
##SC: O(1)

# from typing import List

# import math
# class Solution:
#     def shipWithinDays(self, a: List[int], days: int) -> int:

#         capacity = max(a)
#         total = sum(a)
#         counter_day = 1
#         load = 0
#         while capacity <= total:
#             for k in range(len(a)):
#                 if load + a[k] > capacity:
#                     counter_day = counter_day + 1
#                     load = a[k]
#                 else:
#                     load = load + a[k]
#             if counter_day <= days:
#                 break
#             else:
#                 capacity = capacity + 1
#                 counter_day = 1
#                 load = 0
#         return capacity 
    

##-----------------------------------------------------------------------

##TC:  O(N * log(sum(a[]) - max(a[]) + 1)), 
##SC: O(1)

from typing import List

import math
class Solution:
    def shipWithinDays(self, a: List[int], days: int) -> int:

        start = max(a)
        end = sum(a)
        counter_day = 1
        load = 0
        res = 0
        while start <= end:
            mid = (start+end) // 2
            for k in range(len(a)):
                if load + a[k] > mid:
                    counter_day = counter_day + 1
                    load = a[k]
                else:
                    load = load + a[k]
            if counter_day <= days:
                res = mid
                end = mid - 1
                counter_day = 1
                load = 0
            else:
                start = mid + 1
                counter_day = 1
                load = 0

        return res