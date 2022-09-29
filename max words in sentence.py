sentences=[]
n=int(input("enter the number of sentences:"))
for i in range(n):
    sent=input("enter the sentence:")
    sentences.append(sent)
print(sentences)
maxword=0
cntlist=0
list1=[]
for i in range(n):
    list1=sentences[i].split()
    print(list1)
    cntlist=len(list1)
    if maxword<cntlist:
        maxword=cntlist
    
print("maximum number of words that appear in a single sentence:", maxword)
