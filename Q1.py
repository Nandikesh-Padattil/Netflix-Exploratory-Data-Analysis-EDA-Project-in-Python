a=int(input("Enter first number = "))
b=int(input("Enter second number = "))
c=int(input("Enter third number = "))
if b-a<0:
    if a-c<0:
        print(c,"is the maximum integer")
    elif c-b<0:
        print(a,"is the maximum integer")
    else:
        print(a,"is the maximum integer")
else:
    if b-c<0:
        print(c,"is the maximum integer")
    elif c-a<0:
        print(b,"is the maximum integer")
    else:
        print(b,"is the maximum integer")
