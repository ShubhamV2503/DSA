
## TC: O(N*N) and SC: O(1)


a = [13,46,24,52,20,9]
# a = [1,2,3,4,5,6]  --> if already sorted, it will break early so TC will be O(N)


for i in range(len(a)):
    bool = False
    for j in range(0,len(a)-1):
        if a[j] > a[j+1]:
            copy = a[j]
            a[j] = a[j+1]
            a[j+1] = copy
            bool = True
    if not bool:
        break

print(a)






