

s = "tree"

hashmap = {}

for ch in s:
    if ch not in hashmap:
        hashmap[ch] = 1
    else:
        hashmap[ch] = hashmap[ch] + 1
print(hashmap)



