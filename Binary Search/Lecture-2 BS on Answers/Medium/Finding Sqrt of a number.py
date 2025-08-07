
## Tc: O(sqrt(n))
## Sc: O(1)

# n = 90

# res = 1

# for i in range(1,n//2):
#     res = i*i
#     if res > n:
#         res = (i-1) * (i-1)
#         break
# print((i-1))


#---------------------------------------------------------


## Tc: O(log(n))
## Sc: O(1)

# import math

# def floorSqrt(n):
#     ans = int(math.sqrt(n))
#     return ans

# print(floorSqrt(90))



#---------------------------------------------------------
## TC: O(log(n))
## SC: O(1)

n = 29
start = 1
end = 29

while start <= end:
    mid = (start+end)//2
    val = mid*mid
    if val <= n:
        start = mid +1
    else:
        end = mid - 1

print(end)






