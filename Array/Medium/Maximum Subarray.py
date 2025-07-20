## LeetCode Problem: Maximum Subarray
## LEETCODE: 53

## TC: O(n^3)
## SC: O(1)


# a = [2,1,-3,4,-1,2,1,-5,4]
# a = [1]
# maxi = float('-inf')
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         sum = 0
#         for k in range(i,j+1):
#             sum = sum + a[k]
#             maxi = max(maxi,sum)
#             print(a[k],end=" ")
#         print()
#     print()
# print(maxi)

##----------------------------------------------------------------------------------

## TC: O(n^2)
## SC: O(1)

# a = [2,1,-3,4,-1,2,1,-5,4]

# maxi = float('-inf')

# for i in range(len(a)):
#     sum = 0
#     for j in range(i,len(a)):
#         sum = sum + a[j]
#         maxi = max(maxi,sum)
# print(maxi)



##----------------------------------------------------------------------------------


# ## TC: O(n) --> Kadane's Algo
# ## SC: O(1)

# # a = [-4,0,-3,-2,-1]
# # a = [-4,-3,-2,-1]
# a = [2,1,-3,4,-1,2]

# maxi = float('-inf')
# current_sum = 0
# for i in range(len(a)):
#     current_sum = current_sum + a[i]
#     maxi = max(maxi,current_sum)
#     if current_sum < 0:
#         current_sum = 0

# print(maxi)


##----------------------------------------------------------------------------------

## Print position of max sub array

# ## TC: O(n)
# ## SC: O(1)

# # a = [-4,0,-3,-2,-1]
# # a = [-4,-3,-2,-1]
# a = [2,1,-3,4,-1,2]
a = [2,3,5,1,9]

maxi = float('-inf')
current_sum = 0
start = -1
end = -1
for i in range(len(a)):
    if current_sum == 0:
        temp = i
    current_sum = current_sum + a[i]
    if current_sum > maxi:
        maxi = current_sum
        start = temp
        end = i
    if current_sum < 0:
        current_sum = 0

print(maxi)
print(start,end)
print(sum(a[start:end+1]))