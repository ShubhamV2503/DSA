

## LeetCode 13: Roman to Integer
## Leetcode Problem No. 13
## TC: O(n)
## SC: O(1)

data = {

    'I': 1,
    'V': 5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

print(data)

s = "MCMXCIV"
result = data[s[0]]
for i in range(1,len(s)):
    if data[s[i-1]] >= data[s[i]]:
        result = result + data[s[i]]
    else:
        result = result + (data[s[i]] - 2*data[s[i-1]])
print(result)