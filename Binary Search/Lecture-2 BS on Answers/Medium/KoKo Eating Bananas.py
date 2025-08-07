
## Leetcode Problem: KoKo Eating Bananas
## Problem Link: https://leetcode.com/problems/koko-eating-bananas/
## leetcode Problem Number: 875
##Tc: O(n * max(a)))
##Sc: O(1)


# import math
# a = [3,6,7,11]
# h = 8
# sum = 0
# counter = 1

# while counter <= max(a):
#     sum = 0
#     for k in a:
#         sum = sum + math.ceil(k / counter)

#     if sum <= h:
#         break
#     else:
#         counter = counter + 1

# print(sum,counter)

###-------------------------------------------------------------------------------

##Tc: O(n * log(max(a)))
##Sc: O(1)

import math
a = [30,11,23,4,20]
h = 6
sum = 0
start = 1
res = end = max(a)

while start <= end:
    sum = 0
    mid = (start+end) // 2
    for k in a:
        sum = sum + math.ceil(k / mid)

    if sum <= h:
        res = mid
        end = mid-1
    else:
        start = mid + 1

print(res)






