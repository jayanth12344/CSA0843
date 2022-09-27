sk=[]
n=int(input("number of elements are :"))
for i in range(0,n):
    print("the number :")
    item=int(input())
    sk.append(item)
g=[]
h=[]
for i in sk:
    if i%2==0:
        g.append(i*i)
    else:
        h.append(i*i)
print("[",sum(h),sum(g),"]")
