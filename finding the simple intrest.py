principle_amount=int(input("enter the value of principle:"))
age=int(input("enter the age of customer:"))
if age > 60:
    print("customer is senior citizen")
    rate_of_intrest =12
    print(rate_of_intrest)
elif age < 60:
    print("customer is not senior citizen")
    rate_of_intrest=10
    print(rate_of_intrest)
time_span=int(input("enter the value time span:"))
if time_span < 0:
    print("error : enter the positive number")
    exit()
simple_intrest=(principle_amount *rate_of_intrest *time_span)/100
print(simple_intrest)
