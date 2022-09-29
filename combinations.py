n=int(input("enter the value of n:"))
if n!=3:
    print("enter the  n value equal to 3")
else:
    c=[]
    for i in range(0,n):
        b=int(input("enter the numbers:"))
        c.append(b)
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                if(i!=j&j!=k&k!=i):
                    print(c[i],c[j],c[k])
