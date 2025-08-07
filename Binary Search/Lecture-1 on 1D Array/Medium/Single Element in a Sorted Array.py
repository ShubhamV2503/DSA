


a = [1,1,2,3,3,4,4,8,8]

start = 1
end = len(a)-2

    # Edge cases:
if end == 1:
    print(a[0])
if a[0] != a[1]:
    print(a[0])
if a[end - 1] != a[end - 2]:
    print(a[end - 1])

while start <= end:
    mid = (start+end)//2
    if (a[mid] != a[mid-1]) and a[mid] != a[mid+1]:
        print(a[mid])
        break

    if (a[mid] %2 == 1 and a[mid] == a[mid-1]) or (a[mid] %2 == 0 and a[mid] == a[mid+1]) :
        start = mid + 1
    else:
        end = mid-1

