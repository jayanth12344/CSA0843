try:
    n=int(input("enter the number:"))
    fact=1
    if n<0:
        print("invalid number")
    elif n==0:
        print("zero factorial is :",1)
    
    else:
        for i in range(1,n+1):
            fact=fact*i
        print(fact)
except ValueError:
    print("enter only numbers")
