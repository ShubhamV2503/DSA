## Majority Element in an Array
## LeetCode Problem: https://leetcode.com/problems/majority-element/
## Leetcode Problem Number: 169

## TC: O(n)
## SC: O(n)


# a = [2,2,1,1,1,2,2]


# hashmap = {}

# for num in a:
#     if num not in hashmap:
#         hashmap[num] = 1
#     else:
#         hashmap[num] = hashmap[num] + 1

# max = 0

# for key in hashmap:
#     if hashmap[key] > max:
#         res = key
#         max = hashmap[key]

# print(res)

###----------------------------------------------------------

## TC: O(n log n)
## SC: O(1)

# a = [2,2,1,1,1,2,2]


# a.sort()

# print(a[len(a)//2])

###----------------------------------------------------------

##Tc: O(n)
##Sc: O(1)

a = [2,2,1,1,1,2,2]
counter = 0
candidate = 0

for value in a:
    if counter == 0:
        candidate = value
        counter = counter + 1
    elif value == candidate:
        counter  = counter + 1
    else:
        counter = counter - 1

print(candidate)

        




