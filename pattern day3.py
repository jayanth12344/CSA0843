try:
    rows = int(input("Enter the number of rows:"))  
    k = 2 * rows - 1
    if rows<=0:
        print("enter the values greater than zero")
    else:
        for i in range(0, rows+1):  
            for j in range(0, k):  
                print(end=" ")  
            k = k - 1  
            for j in range(i,0,-1):  
                print(j, end=" ")    
            print("")
except ValueError:
    print("enter the integers only")
