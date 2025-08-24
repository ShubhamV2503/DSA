

def palind(start,end, s):
    while start < end:
        if s[start] != s[end]:
            return 1
        else:
            start = start + 1
            end = end - 1  
    return s[start:end+1]

s = "babad"
start = 0
end = len(s)-1
counter = 0

while counter != len(s)-1:
    start = counter
    end = len(s)-1
    while start < end:
        if s[start] == s[end]:
            res = palind(start,end,s)
        else:
            end = end - 1
    counter = counter + 1














