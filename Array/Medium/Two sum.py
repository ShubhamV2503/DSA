
# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such
# LeetCodeforces Problem: https://codeforces.com/problemset/problem/1/A
## Leetcode problem number: 1

## Time Complexity: O(N^2)
## Space Complexity: O(1)

# a = [2,7,11,15]

# target = 9

# for i in range(len(a)):
#     for j in range(i, len(a)):
#         if a[i] + a[j] == target and i!=j:
#             print(i,j)
#             break
# print(i,j)


###----------------------------------------------------------

## Time Complexity: O(N)
## Space Complexity: O(N)

# a = [3,3]
# # a = [2,7,11,15]

# target = 6
# hashmap = {}

# for i in range(len(a)):
#     hashmap[a[i]] = i

# print(hashmap)

# for i in range(len(a)):
#     if target - a[i] in hashmap and hashmap[target-a[i]] !=i:
#         print(i,hashmap[target-a[i]])
#         break

###----------------------------------------------------------





