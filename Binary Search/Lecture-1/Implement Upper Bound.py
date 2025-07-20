
## TC: O(n)
## SC: O(1)

# a = [1,2,2,3]
# a = [3,5,8,15,19]
# x = 9

# for i in range(len(a)):
#     if a[i] > x:
#         print(i)
#         break

##----------------------------------------------------------------------

## TC: O(log n)
## SC: O(1)
from typing import List

a = [3,5,8,9,15,19]
# a = [1,2,2,3]
x = 9

start = 0
end = len(a)
res = len(a)-1

while start <= end:
    mid = (start+end) // 2
    if a[mid] > x :
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)


