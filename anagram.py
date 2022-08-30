def check(a1,a2):
    if(sorted(a1)==sorted(a2)):
        print("the string is anagram")
    else:
        print("the string is not anagram")

a1=str(input("enter the string a1:"))
a2=str(input("enter the string a2:"))
check(a1,a2)
