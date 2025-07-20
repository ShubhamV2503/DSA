



a1 = [5, 7, 8, 9, 10 ,10 ,11]
a2 = [2, 4, 4 ,6, 6, 8]

union = []

i = 0
j = 0

prev = -1

while i < len(a1) and j<len(a2):
    if a1[i] < a2[j]:
        if len(union) == 0 or union[-1] != a1[i] :  
            union.append(a1[i])
        i = i + 1
    else:
        if len(union) == 0 or union[-1] != a2[j]:
            union.append(a2[j])
        j = j + 1


while i < len(a1):
    if union[-1] != a1[i]:
        union.append(a1[i])
    i =i  + 1

while j < len(a2):
    if union[-1] != a2[j]:
        union.append(a2[j])
    j = j  +1

print('he')
print(union)








