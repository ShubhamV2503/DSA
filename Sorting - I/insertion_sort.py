

a = [14,9,15,12,6,8,13]

counter = 0 

for i in range(len(a)):

    counter = i

    while counter != 0:
        if a[counter-1] > a[counter]:
            temp   = a[counter]
            a[counter] = a[counter-1]
            a[counter-1] = temp
        counter = counter - 1

print(a)


## TC: O(N*N) --> for worst case and SC: O(1)
## TC: O(N)   -> for already sorted array i.e: Best case