
## LeetCode Problem: Find the Smallest Divisor Given a Threshold
## Leetcode Problem Number: 1283

## TC: O(n * max(a))
## SC: O(1)

# import math

# a = [44,22,33,11,1]

# threshold = 5

# counter = 1
# sum = 0

# while counter <= max(a):
#     sum = 0
#     for num in a:
#         sum = sum + math.ceil(num/counter)

#     if sum <= threshold:
#         print(counter)
#         break
#     else:
#         counter = counter + 1


##-------------------------------------------------------------------------

## TC : O(n * log(max(a)))
## SC : O(1)

from typing import List

import math
class Solution:
    def smallestDivisor(self, a: List[int], threshold: int) -> int:

        counter = 1
        sum = 0
        start = 1
        end = max(a)
        res = 0
        while start <= end:
            sum = 0
            mid = (start+end)//2
            for num in a:
                sum = sum + math.ceil(num/mid)

            if sum <= threshold:
                res = mid
                end = mid - 1
            else:
                start = mid+1
        return res


