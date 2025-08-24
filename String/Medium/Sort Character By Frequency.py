
## Leetcode Problem: Sort Characters By Frequency
## Leetcode problem number: 451

##TC: O(n log n) where n is the length of the string
##SC: O(n) for the hashmap

s = "Aabb"
hashmap = {}

for ch in s:
    if ch not in hashmap:
        hashmap[ch] = 1
    else:
        hashmap[ch] = hashmap[ch] + 1
print(hashmap)

hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
print(hashmap)


res = []
for key,freq in hashmap:
    res.append(key*freq)
print("".join(res))

##--------------------------------------------------------------------------------




