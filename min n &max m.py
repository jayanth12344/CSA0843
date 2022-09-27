def add(m1,n1):
    a=m1+n1
    return a
def diff(m1,n1):
    d=m1-n1
    return d
n=eval(input("enter the no of items:"))
list1=[]
list2=[]
for i in range(n):
    no=eval(input("enter the number to check:"))
    list1.append(no)
print(list1)
list1.sort()
print(list1)
m=eval(input("enter the mth max number:"))
n=eval(input("enter the nth max number:"))
m1=list1[-m]
n1=list1[n-1]
c=add(m1,n1)
b=diff(m1,n1)
print("The sum of mth max number and nth min number is:",c)
print("The diff of mth max numer and nth min number is:",b)
