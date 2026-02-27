

a =  [5,5,4,4,6,6,6,5,5,4,4,4,4]

hashmap = {}
max = float('-inf')
stored = []

for i in a:
    if i not in hashmap:
        hashmap[i]  = 1
    else:
        hashmap[i] = hashmap[i]  + 1

print(hashmap)

for key in hashmap:
    if  hashmap[key] >= max:
        max = hashmap[key]
        if len(stored) > 0:
            if hashmap[stored[0]] == max:
                if stored[0] > key:
                    stored[0] = key
            else:
                if hashmap[stored[0]] < max:
                    stored[0] = key
        else:
            stored.append(key)
        
print(stored)


#TC: O(N)
# SC: O(N) in worst case only


