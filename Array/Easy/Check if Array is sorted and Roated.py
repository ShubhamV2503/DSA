


a = [3,4,5,1,2]
smaller = float('inf')
bool = False

for i in range(len(a)):
    if a[i] < smaller:
        smaller = a[i]
        index = i
print(index)

counter = index
array = []

while counter !=len(a):
    for i in range(counter,len(a)):
        array.append(a[i])
        counter = counter + 1
    print(array)





