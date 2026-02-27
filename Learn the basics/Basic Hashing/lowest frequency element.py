


a = [10,5,10,15,10,5]

hashmap = {}

for i in a:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1
print(hashmap)


max = float('-inf')
min = float('inf')

for key in hashmap:
    if hashmap[key] > max :
        max = hashmap[key]
    else:
        min = hashmap[key]
print(max , min)


