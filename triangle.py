s=float(input("enter the staring number:"))
rows =int(input("Enter number of rows: "))
number =s
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("%.1f"%number, end=" ")
        number+=0.1
    print()
