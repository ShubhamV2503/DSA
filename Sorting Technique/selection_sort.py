

a = [13,46,24,52,20,9,9]

temp = 0
smaller = float('inf')
for start_index in range(len(a)):
    for j in range(start_index,len(a)):
        if a[j] < smaller:
            smaller = a[j]
            smaller_index = j

    temp = a[start_index]
    a[start_index] = smaller
    a[smaller_index] = temp
    smaller = float('inf')
print('My sorted array',a)


## TC: O(N*N) and SC: O(1)



