try:
    n=int(input("enter the vlaue of n:"))
    if n<0:
        print("enter the positive number:")
    elif n>=18:
        print("eligible for vote")
    else:
        r=18-n
        print("eligible for vote after :",r)
except ValueError:
    print("enter the integer alues only") 
