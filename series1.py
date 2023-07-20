# 4 3 2 1
# 4 3 2
# 4 3
# 4

i = 1 
j = 4 
l = j
while i <=j:
    k = 1
    c = l
    while k <= l:
        print(c,end = ' ')
        k = k + 1
        c = c - 1
    i = i + 1
    l = l - 1
    print()