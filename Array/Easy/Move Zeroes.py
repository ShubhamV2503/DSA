
## Leetcode Problem: https://leetcode.com/problems/move-zeroes/
## Problem Statement: Given an integer array nums, move all 0's to the end
## Problem Number: 283
## Difficulty: Easy

# a = [0,1,0,3,12]
a =  [ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1 ]

non_zero_index = 0

pointer = 0

if len(a) >1 :

    for i in range(len(a)):
        if a[i] != 0:
            non_zero_index = i
            break

    while non_zero_index < len(a):
        if a[pointer] == 0 and a[non_zero_index] !=0 :
            a[pointer] = a[non_zero_index]
            a[non_zero_index] = 0
            pointer = pointer + 1
            non_zero_index = non_zero_index + 1
        elif a[pointer] == 0 and a[non_zero_index] == 0:
            non_zero_index = non_zero_index + 1
        else:
            pointer = pointer + 1
            non_zero_index = non_zero_index + 1

print(a)

## TC: O(N)
## SC: O(1)


###-------------------------< > ###########################



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        for i in nums:
            if i !=0:
                nums[index] = i
                index = index + 1


        while(index < len(nums)):
            nums[index] = 0
            index = index +1 





## TC: O(N)
## SC: O(1)

###-------------------------< > ###########################
