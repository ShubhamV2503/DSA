
# ## TC = O(N) and SC = O(N)

# a = [3, 1, 2, 3, 2]

# hashmap = [0]* a.max()

# for i in a:
#     hashmap[i] = hashmap[i] + 1
# print(hashmap)

#--------------------------------------------------------------#

# ## TC = O(Log(N)) for Ordered Map and SC = O(N)

# a = [3, 1, 2, 3, 2]

# map = {}

# for i in range(len(a)):
#     if a[i] not in map:
#         map[a[i]] = 1
#     else:
#         map[a[i]] = map[a[i]] + 1

# print(map)

#--------------------------------------------------------------#




hashmap = {}

nums = [1,4,8,13]
k = 5
for i in range(len(nums)):
    while (k > 0):
        if nums[i] not in hashmap:
            k  = k - 1
            nums[i] = nums[i]  +1
        else:
            hashmap[nums[i]] = hashmap[nums[i]]  + 1

print(hashmap)     

# hashmap = {}
# for i in range(len(nums)):
#       while k > 0:
#               if nums[i] not in hashmap:
#                     k = k - 1
#                     nums[i] = nums[i] + 1
#                 else:
#                     hashmap[nums[i]] = hashmap[nums[i]] + 1




