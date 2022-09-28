def print_factors(x):
    cnt=0
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           cnt=cnt+1
           if (cnt==m):
               break
       
n=int(input("Enter the value of N : "))
m=int(input("enter the number of factors M :"))
count=0
a=1;
fact1=[]
while count<n:
    sum=0
    for b in range (1,(a//2)+1):
        if a%b==0:
            sum=sum+b
    if sum==a:
        print("\n",a ,end=' ')
        fact1.append(a)
        count+=1
    a+=1

for i in fact1:
    print_factors(i)
