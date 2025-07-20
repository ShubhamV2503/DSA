
## Problem Statement:
# Given an array of integers from 0 to n, find the missing number in the array
## leetcoode problem: https://leetcode.com/problems/missing-number/
# Leetcdode problem number: 268

#TC: O(n)
#SC: O(n)

# a = [2,0,1]

# hashmap = {}

# max = float('-inf')

# for num in a:
#     if num >  max :
#         max = num

# for num in a:
#     if num not in hashmap:
#         hashmap[num] = 1
#     else:
#         hashmap[num] = hashmap[num]  + 1

# counter = 0

# while counter  < len(a)+1:
#     if counter not in hashmap:
#         print(counter)
#         break
#     else:
#         counter = counter + 1


## #----------------------------------------- ##

#TC: O(n)
#SC: O(1)


class Solution:
    def missingNumber(self, a: List[int]) -> int:
        max = float('-inf')

        check = 0
        for num in a:
            if num > max :
                max = num
        array_sum = 0
        for k in a:
            array_sum = array_sum + k
            if k == 0:
                check = check + 1

        sum = max * (max + 1) /2

        if(int(sum-array_sum)) == 0 and check!=0:
            return (max+1)
        elif int(sum-array_sum) == 0 and check==0:
            return 0
        return int(sum-array_sum)

