

a = [1,2,3,4,5]

small = a[0]
greater = a[0]

bool = False

for i in range(len(a)):
    for j in range(0,len(a)-1):
        if a[j] >  a[j+1]:
            bool = True
    if bool is not False:
        print("not sorted")
    else:
        print("sorted")




