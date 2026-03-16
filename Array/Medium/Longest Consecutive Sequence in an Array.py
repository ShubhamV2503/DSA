
# a  = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

# a.sort()

# maxi = 0
# counter = 0

# for i in range(len(a)-1):

#     if a[i] == a[i+1]:   # skip duplicates
#         continue

#     elif a[i] + 1 == a[i+1]:
#         counter += 1

#     else:
#         maxi = max(maxi, counter)
#         counter = 0

# maxi = max(maxi, counter)
# print(maxi + 1)

# TC: O(N*LogN)
# SC: O(N)

########################################################


a  = [0, 3, 7, 0, 1]

s = set(a)
print(s)


# TC: O(N)
# SC: O(N)