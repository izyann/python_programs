j = int(input("enter the number:"))
n = 3
while n <= j:
    i = 2 
    count = 1
    while i < n:
        if n  % i == 0:
            count += 1
        i += 1
    if count==1:
        print(n)
    n = n + 1