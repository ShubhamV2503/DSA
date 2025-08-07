

a = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
target = 3

start = 0
end = len(a)-1
bool = False
while start<=end:
    mid = (start+end)//2
    if a[mid] <= target <= a[end]:
        if a[mid] == target:
            bool = True
            break
        start = mid
    else:
        end = mid - 1

print(bool)