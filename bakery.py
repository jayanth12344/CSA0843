a=float(input("enter the no;of fresh loave purchased:"))
if a==-1:
    print("invalid number")
else:
    b=float(input("enter the no;of old loave purchased:"))
    c=185
    flv_price=c*a
    olv_price=((60*c)/100)*b
    print("regular price is =""{:.2f}".format(c))
    print('amount of new loaves = :'"{:.2f}".format(flv_price))
    print('amout of old loaves = :'"{:.2f}".format(olv_price))
    print('total amount =',"{:.2f}".format(flv_price+olv_price))
