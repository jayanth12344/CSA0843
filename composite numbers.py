n=int(input("starting element:"))
m=int(input("enter the last element:"))
for num in range(n,m+1):
    c=0
    for i in range(1,num):
        if num%i==0:
            c=i
    if c>2:
        print(num)  
    
