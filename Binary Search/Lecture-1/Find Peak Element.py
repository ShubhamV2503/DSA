
## LeetCode 162: Find Peak Element
## leetcode https://leetcode.com/problems/find-peak-element/
## TC: O(n)
## SC: O(1)


nums = [1,2,1,3,5,6,4]

prev = 0
current = 1
maxi = 0

for i in range(len(nums)-1):
    if nums[prev] < nums[current]:
        maxi = max(maxi,current)
        prev = prev +1
        current = current + 1
    else:
        prev = prev + 1
        current = current + 1
print(maxi)
