import statistics
n=int(input("enetr the value:"))
list=[]
for i in range(n):
    b=int(input("enter the elemnts:"))
    list.append(b)
list.sort()
print(list)
print("mean is %s"%(statistics.mean(list)))
print("median is %s"%(statistics.median(list)))
print("mode is %s"%(statistics.mode(list)))
