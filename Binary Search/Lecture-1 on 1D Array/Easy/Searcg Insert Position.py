
## LeetCode 35: Search Insert Position
## Tc: O(n) 
## Sc: O(1)


# nums = [1,3,5,6]
# target = 7
# res = len(nums)

# for i in range(len(nums)):
#     if nums[i] >= target:
#         res = i
#         break
# print(res)

##--------------------------------------------------- Alternative Solution using Binary Search
## Tc: O(log n)
## Sc: O(1)


def searchInsert(arr, x) -> int:
    n = len(arr)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans



