


a = [1,2,3,4,5,6,7]

############ right rotate array by 1

# temp = a[0]

# for i in range(1,len(a)):
#     a[i-1] = a[i]
# a[i] = temp
# print(a)

k = 3
a.reverse()
print(a)
a[:k] = reversed(a[:k])
print(a)
a[k:] = reversed(a[k:])
print(a)




