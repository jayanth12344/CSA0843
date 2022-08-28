number=int(input("enter the numbers:"))
if number<0:
    print("enter the numbers")
else:
    sum=0
    while(number>0):
            sum+=number
            number-=1
    print("the sum is :",sum)
