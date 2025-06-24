
a = [14,9,15,12,6,8,13]
res = []


def merge_sort(left_array, right_array):
    
    i,j = 0,0
    res = []

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            res.append(left_array[i])
            i = i + 1
        else:
            res.append(right_array[j])
            j = j + 1

    while i <  len(left_array):
        res.append(left_array[i])
        i = i + 1
    
    while j < len(right_array):
        res.append(right_array[j])
        j = j  + 1

    return res


def divide(a):
    if len(a) <= 1:
        return a
    
    mid = len(a) // 2
    left_array = divide(a[:mid])
    right_array = divide(a[mid:])

    return merge_sort(left_array,right_array)

print(divide(a))

