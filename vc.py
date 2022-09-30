string=str(input("enetr the string:"))
for i in string:
    if i in "aeiouAEIOU":
        print("vowels are",i)
    else:
        print("consonants are",[i])


