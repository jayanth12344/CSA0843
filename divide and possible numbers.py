n=int(input("enter the value of n:"))
m=int(input("enter the value of m:"))
c=0
for i in range(1,max(n,m)+1):
    if (n%i==0) and (m%i==0):
        c+=1
print(c)        
