
# a = [0,0,1,1,1,2,2,3,3,4]

# hashmap = {}

# for i in a:
#     if i not in hashmap:
#         hashmap[i] = 1
#     else:
#         hashmap[i] = hashmap[i] + 1

# print(hashmap)

# counter = 0
# for j in hashmap:
#     a[counter] = j
#     counter = counter + 1
# print(a)


# my_set = set()  # Don't name it 'set' to avoid shadowing the built-in type

# for i in a:
#     my_set.add(i)

# print(my_set)

# counter = 0
# for j in my_set:
#     a[counter] = j
#     counter = counter + 1
# print(a)

## TC: O(NLogN)
## SC: O(N)

############ above 2 method is brute force ###########################


######### Below is optimal approach ################

## TC: O(N)
## SC: O(1)


a = [0,0,1,1,1,2,2,3,3,4]


i = 0
j = 1
while j !=len(a):
    if a[i] != a[j]:
        a[i+1] = a[j]
        i = i + 1
    j = j  + 1

print(a)
print(i+1)




