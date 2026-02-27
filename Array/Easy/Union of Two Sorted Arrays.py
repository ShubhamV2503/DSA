


#############   Map technique #########################


# a1 = [5, 7, 8, 9, 10 ,10 ,11]
# a2 = [2, 4, 4 ,6, 6, 8]

# hashmap = {}


# for i in range(len(a1)):
#     hashmap[a1[i]] = hashmap.get(a1[i],0)+1

# for i in range(len(a2)):
#      hashmap[a2[i]] = hashmap.get(a2[i],0)+1

# res = [0]*len(hashmap)
# index = 0
# for key in hashmap:
#      res[index] = key
#      index = index + 1

# res.sort()
# print(res)


# 📌 Final Answer:

# Time Complexity: O(n + m + k log k)
# Space Complexity: O(k)
# Worst Case: TC = O((n+m) log(n+m)), SC = O(n+m)


##################################################



################### Set technique  ####################

# a1 = [5, 7, 8, 9, 10 ,10 ,11]
# a2 = [2, 4, 4 ,6, 6, 8]

# for k in a2:
#     a1.append(k)

# print(a1)
# s1 = set(a1)

# print(s1)


# Time Complexity: O(n + m)
# Space Complexity: O(n + m)


### 2nd version of this using in-built fun

a1 = [5, 7, 8, 9, 10 ,10 ,11]
a2 = [2, 4, 4 ,6, 6, 8]

st = set(a1) | set(a2)
print(sorted(st))


# Time Complexity: O(n + m + k log k)
# Space Complexity: O(n + m)

##################################################

# a1 = [5, 7, 8, 9, 10 ,10 ,11]
# a2 = [2, 4, 4 ,6, 6, 8]

# union = []

# i = 0
# j = 0

# prev = -1

# while i < len(a1) and j<len(a2):
#     if a1[i] < a2[j]:
#         if len(union) == 0 or union[-1] != a1[i] :  
#             union.append(a1[i])
#         i = i + 1
#     else:
#         if len(union) == 0 or union[-1] != a2[j]:
#             union.append(a2[j])
#         j = j + 1


# while i < len(a1):
#     if union[-1] != a1[i]:
#         union.append(a1[i])
#     i =i  + 1

# while j < len(a2):
#     if union[-1] != a2[j]:
#         union.append(a2[j])
#     j = j  +1

# print('he')
# print(union)








