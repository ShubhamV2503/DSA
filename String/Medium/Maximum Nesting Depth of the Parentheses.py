
## Leetcode Problem: Maximum Nesting Depth of the Parentheses
## Leetcode Problem Number: 1614

##Tc: O(n)
##Sc: O(1)

string = "(1+(2*3)+((8)/4))+1"

counter = 0
res = 0
maxi = float('-inf')
for s in string:
    if s == '(':
        counter = counter + 1
    if s == ')':
        counter = counter - 1
    
    maxi = max(maxi,counter)

print(maxi)


