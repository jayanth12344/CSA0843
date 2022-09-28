n=0
i=0
li1=[]
li2=[]
while(n!=-1):
    n=int(input())
    if(n==-1):
        break
    if(n>0):
        li1.append(n)
    else:
        li2.append(n)
avg=sum(li1)/len(li1)
avg1=sum(li2)/len(li2)
print("average of positive numbers is ",avg)
print("average of negative numbers is ",avg1)
