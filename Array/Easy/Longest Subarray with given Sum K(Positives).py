
# a = [2,3,5,1,9]
# m = 10

# sub_length = 0

# for i in range(len(a)):
#     for j in range(i, len(a)):
#         sum = 0
#         for k in range(i,j+1):
#             sum = sum + a[k]
#         if sum == m:
#             sub_length = max(sub_length , j-i+1)
# print(sub_length)


# Time Complexity: O(N^3) approx., where N = size of the array.
# Reason: We are using three nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.


## <------------------------------------------------------------------------------->


# a = [2,3,5,1,9]
# k = 10

# a = [2,3,5]
# k = 5

# sum = 0
# sub_length = 0

# for i in range(len(a)):
#     sum = 0
#     for j in range(i,len(a)):
#         sum = sum  + a[j]
#         if sum == k :
#             sub_length = max(sub_length,  j-i+1)

# print(sub_length)


#TC: O(N*N)
#SC: O(1)

## <------------------------------------------------------------------------------->

# a = [2,3,5,1,9]
# k = 10
# a.sort()
# print(a)




## <------------------------------------------------------------------------------->








