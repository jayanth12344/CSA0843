lower_range=int(input("enter the lower value:"))
upper_range=int(input("enter the upper value:"))
for num in range(lower_range, upper_range+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
              print( '            ',   num)

for num in range(lower_range,upper_range+1):
    count=0
    for j in range(2,num):
        if num%j==0:
            count+=1
    if count>=1:
        print(num)

    

                
    
