

# TC: O(N) and SC: O(1)

a = [1,2,4,7,7,5]

greater = float('-inf')

for i in a:
    if i >= greater:
        greater = i

second = float('-inf')

for j in a :
    if j != greater and j > second:
        second = j
print(second)




