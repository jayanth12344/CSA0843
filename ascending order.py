myList=[]
nums = int(input("enter the number of words:"))
for i in range(nums):
    word=input("enter the word:")
    myList.append(word)
print(myList)    
myList.sort()
print('List in Ascending Order: ', myList)

myList.sort(reverse=True)
print('List in Descending Order: ', myList)
