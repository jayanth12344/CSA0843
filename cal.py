def power(x,n):
    return x**n
def add(x,n):
    return x+n
def sub(x,n):
    return x-n
def mul(x,n):
    return x*n
def div(x,n):
    return(x/n)
while True:
    choice=input("enter the choice(1,2,3,4,5):")
    if choice in ("1","2","3","4","5"):
        a=float(input("enter the value of a:"))
        b=float(input("enter the alue of b:"))
        if choice=="1":
            print(a,"+",b,"=",add(a,b))
        elif choice=="2":
            print(a,"-",b,"=",sub(a,b))
        elif choice=="3":
            print(a,"*",b,"=",mul(a,b))
        elif choice=="4":
            print(a,"/",b,"=",div(a,b))
        elif choice=="5":
            print(a,"**",b,"=",power(a,b))

        
             
        
