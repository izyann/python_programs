n = int(input("enter the number:"))
i = 2 
count = 0
while i < n:
    if n % i ==0:
        count += 1
    i += 1
if count==0:
    print("it is a prime number")
else:
    print("this is not a prime number")