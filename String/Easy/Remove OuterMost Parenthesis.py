
### Given a valid parentheses string s, consider its outermost parentheses.
## Leetcode Problem number: 1021

##TC: O(n*n)
##SC: O(n)


# s = "(()())(())"

# counter = 0
# res = ''
# start = 0
# for i in range(len(s)):
#     if s[i] == '(':
#         counter = counter + 1
#     if s[i] == ')':
#         counter = counter - 1
#     if counter == 0:
#         for k in range(start+1,i):
#             res = res + s[k]
#         start = i+1
# print(res)


##---------------------------------------------------------------------


##TC: O(n)
##SC: O(n)


s = "(()())(())"

counter = 0
res = []
start = 0
for i in range(len(s)):
    if s[i] == '(':
        counter = counter + 1
    if s[i] == ')':
        counter = counter - 1
    if counter == 0:
        for k in range(start+1,i):
            res.append(s[k])
        start = i+1
print(''.join(res))
        