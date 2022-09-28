myList= []
length = int(input("enter the number of elements:"))
even=0
odd=0
for i in range(0,length):
    value =int(input())
    myList.append(value)
print("even numbers are:")
for element in myList:
    if element%2 == 0:
        print(element)
        even =even+(element**2)

print("odd numbers are:")
for element in myList:
    if element%2 != 0:
        print(element)
        odd = odd+(element**2)
print("even sum square is :",even)
print("odd sum square is :",odd)
        

