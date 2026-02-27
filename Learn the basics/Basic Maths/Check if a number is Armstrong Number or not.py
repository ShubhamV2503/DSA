## It was available on Leetcode but its was paid

## Mine code

n = 153
temp = n
res = 0

digits = len(str(n))

while n > 0:
    rem = n % 10
    n = n // 10
    res =res + rem ** digits

print(res)

if res == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



# Time Complexity: O(Log n)
# Space Complexity : O(1)  