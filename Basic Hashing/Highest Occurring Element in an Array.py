

a =  [1, 2, 2,2,2, 3, 3, 3]

hashmap = {}
max = float('-inf')

for i in a:
    if i not in hashmap:
        hashmap[i]  = 1
    else:
        hashmap[i] = hashmap[i]  + 1
        if hashmap[i] > max:
            max = hashmap[i]
            key = i
print(hashmap)
print(max,key)




