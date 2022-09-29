try:
    n=int(input("enter the year:"))
    #k=float(n)
    if n<=0:
         print("enter the positive integer greater than zero")
    elif n%4==0:
        print(n,"is a leap year")
    else:
        print(n,"is not a leap year")
except ValueError:
    print("enter the integer value only")
