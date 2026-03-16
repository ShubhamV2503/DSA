
# Time Complexity: O(N^2)
# Space Complexity: O(N) 


# a = [10, 22, 12, 3, 0, 6]
# a = [4,4,6,0]
# res = []
# bool = False
# for i in range(len(a)):
#     for k in range(i+1,len(a)):
#         if a[i] < a[k]:
#             bool = True
#     if bool is False:
#         res.append(a[i])
#     else:
#         bool = False

# print(res)


#--------------------------------------------------

#TC: O(N)
#SC: O(N)

a = [10, 22, 12, 3, 0, 6]

maxi = a[len(a)-1]
res = []
for i in range(len(a)-1,-1,-1):
    if a[i] >= maxi:
        res.append(a[i])
        maxi = a[i]

print(res)

