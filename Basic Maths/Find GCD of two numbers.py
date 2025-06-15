## Mine code


n1 = 20
n2 = 15
gcd = 1

if n1 > n2:
    smaller = n2
else:
    smaller = n1

for i in range(1, smaller +1 ):
    if n1 %i ==0 and n2 % i  == 0:
        if i > gcd:
            gcd = i 
print("The GCD of", n1, "and", n2, "is", gcd)



# Time Complexity: O(min(N1, N2)) 
# Space Complexity : O(1)