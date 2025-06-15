## Below is Mine code which i thought and did myself

n = 0

i = 1
count = 1

while n - i > 0:
    i = i * 10
    count += 1

print("Number of digits in the number is:", count)


# Time Complexity: O(log n)
# Space Complexity : O(1)

#-------------------------------------------------------------------------------#

## Below is the code from striver 
                                
                     
import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.
def countDigits(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt

# Main function
if __name__ == "__main__":
    N = 329823
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)

                                
# Time Complexity: O(1)
# Space Complexity : O(1)                     
                                
                     


                                
                            