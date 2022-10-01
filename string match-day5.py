def diff_position(string1,string2):
    a=string1.replace(' ','')
    b=string2.replace(' ','')
    if len(a)<len(b):
        length=len(a)
    else:
        length=len(b)
    count=0
    for i in range(length):
        if a[i]!=b[i]:
            count=count+1
    print(length-count)
print("enter the name of the string1 :")
string1=str(input())
print("enter the name of the string2 :")
string2=str(input())
print("The Matches between the two strings are:")
diff_position(string1,string2)
