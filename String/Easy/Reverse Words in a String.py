
##LeetCode Problem: Reverse Words in a String
##Leetcode problem number: 151

##TC: O(n*n)
##SC: O(n)


# s = "the sky is blue"

# s = s.split(' ')
# k = ''
# for st in range(len(s)-1,-1,-1):
#     if len(s[st])>0:
#         k = k + s[st]+' '
# print(k.strip())


##-----------------------------------------------------------

##Tc: O(N)
##SC: O(N)

s = "the sky is blue"

s = s.split(' ')
 
k = []
for st in range(len(s)-1,-1,-1):
    if len(s[st])>0:
        k.append(s[st]+' ')
# print(k.strip())
print(' '.join(k))


