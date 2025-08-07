
##Leetcode 1482. Minimum Days to Make M Bouquets

## TC: O(n × D) = O(n × (max(a) - min(a) + 1))
## SC: O(1)

# a = [7,7,7,7,12,7,7]
# m = 2
# k = 3


# day = min(a)
# counter = 0
# sum = 0

# if len(a) < m*k:
#     print(-1)
# else:
#     while day <= max(a):
#         counter = 0
#         sum = 0
#         for num in a:
#             if day >= num:
#                 counter = counter + 1
#             else:
#                 sum = sum + counter // k
#                 counter = 0
#         sum = sum + counter //k
#         if sum >= m:
#             print('poss')
#             break
#         else:
#             print('not poss')
#             day = day + 1



###-----------------------------------------------------------------------

##Tc: O(n log(max(a) - min(a))) 
##SC: O(1)


# a = [62,75,98,63,47,65,51,87,22,27,73,92,76,44,13,90,100,85]
# m = 2
# k = 7


# day = min(a)
# counter = 0
# sum = 0

# start = min(a)
# end = max(a)
# res = 0

# if len(a) < m*k:
#     print(-1)
# else:
#     while start <= end:
#         mid = (start+end) // 2

#         day = mid
#         counter = 0
#         sum = 0
#         for num in a:
#             if day >= num:
#                 counter = counter + 1
#             else:
#                 sum = sum + counter // k
#                 counter = 0
#         sum = sum + counter //k
#         if sum >= m:
#             res = day
#             end = mid - 1
#         else:
#             start = mid + 1
# print(res)