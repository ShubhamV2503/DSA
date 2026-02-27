
s = "aabcb"
substrings = []

hashmap = {}

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substrings.append(s[i:j])
print(substrings)

for k in substrings:
    if len(k) != 1:
        for i in k:
            if i not in hashmap:
                hashmap[i] =1
            else:
                hashmap[i] = hashmap[i] +1
        print(hashmap)
        hashmap = {}
    

