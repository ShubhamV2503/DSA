


a = [2,2,3,3,4,4,4] 
target = 3

def first():
    first_index = len(a)
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start+end) // 2
        if a[mid] >= target:
            first_index = mid
            end = mid-1
        else:
            start = mid +1 

    return(first_index)


def last():
    last_index = len(a)
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start+end) // 2
        if a[mid] > target:
            last_index = mid
            end = mid-1
        else:
            start = mid +1 

    return(last_index)

print('last=',last())
print('first=',first())
print(last()-first())
