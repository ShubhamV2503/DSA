

# s = "0-1"
s = "words and 987"
# s = "   -042"

res = []

INT_MAX = 2**31 - 1
INT_MIN = -2**31

sign = 1
i = 0
while i< len(s) and s[i] != ' ':
    i = i + 1

if i < len(s):
    print('yes')
else:
    print('no')