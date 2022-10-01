n=str(input("enter the string:"))
m=int(input("enter the rows number:"))
if m<=0:
    print("enter number greater than zero:")
else:
    for i in range(1,m+1):
        for j in range(1,i+1):
            print(n,end="")
        print()    
