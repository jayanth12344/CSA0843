Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input("Enter length of the list:"))
c=[]
e=[]
if(a>0):
    for i in range(0,a):
        b=int(input("enter element:"))
        c.append(b)
    for i in range(0,a):
        b=0
        for j in range(0,a):
            if(c[j]<c[i]):
                b=b+1
        e.append(b)
    print("INPUT=",c)
    print("OUTPUT",e)
else:
    print("INVALID INPUT")