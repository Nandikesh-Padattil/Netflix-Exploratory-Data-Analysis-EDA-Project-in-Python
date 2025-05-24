n=int(input("Enter Number to be checked = "))
a=str(n)
q=list(a)
c=0
for i in q:
    w=int(i)
    b=pow(w,3)
    c=c+b
if c==n:
    print("yes it an armstrong number")
else:
    print("no it is not an armstrong number")

