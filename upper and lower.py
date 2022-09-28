str=input('enter the word: ')
lower=0
upper=0
number=0
spec=0
if str=='*':
    print("stop the program")
else:
    for i in str:
        if (i.islower()):
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            print(i)
            number+=1
        else:
            spec+=1
    print ("the number of lowercase characters is:", lower)
    print ("the number of uppercase characters is: ", upper)
    print("the number of number count is:",number)
