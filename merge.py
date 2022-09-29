n=int(input("enter the value of n:"))
m=int(input("enter the value of m:"))
list1=[]
list2=[]
list3=[]
for i in range(1,n+1):
    b=int(input("enter the values in list1:"))
    list1.append(b)
for j in range(1,m+1):
    c=int(input("enter the values of list2:"))
    list2.append(c)
list3=list1+list2
print(list3)
