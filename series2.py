# 1 2 3 4
# 2 3 4
# 3 4
#4
i = 1 
j = 4
l = j
while i <= j:
    k = 1
    c = i
    while k <= l:
        print(c,end = ' ')
        k = k + 1
        c = c + 1
    i = i + 1
    l = l -1
    print()