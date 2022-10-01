try:
    n=int(input("ENTER NUMBER OF ELEMENTS----> "))
    print("\n")
    arr=[]
    for i in range(0,n):
        a=int(input("enter the number:-"))
        arr.append(a)
    if(arr[i]<0):
        print("NEGATIVE")
        exit()
    pcount=0
    ccount=0
    f=0
    plist=[]
    clist=[]
    for i in range(0,n):
        f=0
        for j in range(2,arr[i]):
            if(arr[i]%j==0):
                f=f+1
        if(f==0):
            pcount+=1
            plist.append(arr[i])
        else:
            ccount+=1
            clist.append(arr[i])
    print("PRIME COUNT--> ",pcount)
    print("COMPOSITE COUNT--> ",ccount)
    print("PRIME LIST---> ",plist)
    print("COMPOSITE LIST---> ",clist)
except ValueError:
    print("ERROR 1")
