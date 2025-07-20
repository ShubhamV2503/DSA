

a = [1,8,10,1]


bool = False


for j in range(0,len(a)-1):
    if a[j] >= a[j+1]:
        bool = True
        break

if bool is not False:
    print("not sorted")
else:
    print("sorted")




