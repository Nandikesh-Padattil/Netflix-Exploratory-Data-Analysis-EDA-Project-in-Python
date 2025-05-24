n=int(input("First Number = "))
m=int(input("Second Number = "))
c=0
a=0
for i in range(1,(n//2)+1):
    if n%i==0:
        c=c+i
if c==m:
    for i in range(1,m//2+1):
        if m%i==0:
            a=a+i
else:
    print("Not Amicable")
if a==n and c==m:
    print("Is Amicable")
            
