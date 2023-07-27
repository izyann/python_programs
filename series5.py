s = 0 
n = int(input("enter the number"))
while 0 <  n:
    r = n % 10
    n = n // 10
    s = s * 10 + r
print(s)