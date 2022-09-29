num = input("Enter any value : ")
try:
    val =str(num)[::-1]
    print("Reverse of the given number is : ", val)
except ValueError:
    print("It not a valid value")
