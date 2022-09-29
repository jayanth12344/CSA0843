total_users=int(input("enter the total users: "))
if total_users < 0:

    print("enter valid number")

    exit()
    
staff_users=int(input("enter the staff users: "))    
student_user = (total_users - ((staff_users)/3 + staff_users))
print("the student users are: ",student_user)
