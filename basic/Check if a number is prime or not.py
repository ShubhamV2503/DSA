## Mine code


n = 11
flag = 0

if n < 2:
    print(f"{n} is not a prime number")
elif n == 2:
    print(f"{n} is a prime number")
else:
    for i in range(2,n-1):
        if n % i == 0:
            flag = 1
            break
    if flag == 1:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")


# Time Complexity: O(n)
# Space Complexity : O(1)  