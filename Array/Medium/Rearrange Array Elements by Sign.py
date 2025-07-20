## LeetCode# Rearrange Array Elements by Sign
## Leetcode Problem Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
## Leetcode Problem Number: 2149

## TC: O(n)
## SC: O(n)

a = [3,1,-2,-5,2,-4]
pos = []
neg = []
for num in a:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
print(pos)
print(neg)
pc = 0
nc = 0
for i in range(len(a)):
    if i %2 ==0:
        a[i] = pos[pc]
        pc = pc +1
    else:
        a[i] = neg[nc]
        nc = nc + 1
print(a)





