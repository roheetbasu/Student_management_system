# from SRC import *
import os
import sys
import json
# Adjusting the sys.path to inlcude the SRC Directory
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_dir,"SRC"))

from SRC import *

print(f"----------------Student Management System-------------------")

file_path = 'D:\\Python\\Project1\\Data_storage\\TeacherData.json'
if not os.path.exists(file_path):
    print("Please enter the details for First Teacher:")
    teachercode.Entry4Teacher()
elif os.path.getsize(file_path) == 0:
    print("Please enter the details for First Teacher:")
    teachercode.Entry4Teacher()
else:
    Detail = input("Please enter are you student or teacher?:")
    if Detail.upper() == "STUDENT":
        print("Please Enter your login details---------")
        Name = input(f"Name:")
        roll = int(input("Roll.no:"))
        try:
            if authentication.authentication_for_students(Name,roll):
                print(f'Loading your details------')
                Studentcode.search(Name,roll)
            else:
                raise Exception_handling.AuthenticationErrorforStudent(Name,roll)
        except Exception_handling.AuthenticationErrorforStudent as e:
            print(e.message)
                       
    elif Detail.upper() == "TEACHER":
        print("Please Enter your login details---------")
        Name = input(f"Name:")
        ID = int(input("ID:"))
        try:
            if authentication.authentication_for_teacher(Name,ID):
                print(f'Press \n 1. To add new teacher details \n 2. To add Students details')
                print(' 3. To display details of all Teachers \n 4. To display details of all Students')
                print(' 5. To remove Teachers details \n 6. To remove students details ')
                print(' 7. To search specific Teacher details \n 8. To search specific students details ')
                val = int(input("Enter digit:"))
                if val == 1:
                    count = 'y'
                    while count == 'y':
                        teachercode.Entry4Teacher()
                        count = input("press y to continue and n to exit:")
                        
                elif val == 2:
                    count = 'y'
                    while count == 'y':
                        Studentcode.Entry4students()
                        count = input("press y to continue and n to exit:")
                elif val == 3:
                    teachercode.Display_all()
                elif val == 4:
                    Studentcode.Display_all()
                elif val == 5:
                    teachercode.Delete()
                elif val == 6:
                    Studentcode.Delete()
                elif val == 7:
                    s_name = input("Enter name:")
                    s_ID = int(input("Enter ID:"))
                    try:
                        if authentication.authentication_for_teacher(s_name,s_ID):
                            print(f'Loading your details------')
                            Studentcode.search(s_name,s_ID)
                        else:
                            raise Exception_handling.AuthenticationErrorforStudent(s_name,s_ID)
                    except Exception_handling.AuthenticationErrorforStudent as e:
                        print(e.message)
                elif val == 8:
                    s_name = input("Enter name:")
                    s_roll = int(input("Enter Roll.no:"))
                    try:
                        if authentication.authentication_for_students(s_name,s_roll):
                            print(f'Loading your details------')
                            Studentcode.search(s_name,s_roll)
                        else:
                            raise Exception_handling.AuthenticationErrorforStudent(s_name,s_roll)
                    except Exception_handling.AuthenticationErrorforStudent as e:
                        print(e.message)
                else:
                    print("Invaid Input")
            else:
                raise Exception_handling.AuthenticationErrorforTeacher(Name,ID)
        except Exception_handling.AuthenticationErrorforTeacher as e:
            print(e.message)
    
    else:
        print("Invalid data")
        

print("--------------You have exited the Student Management System------------------")
        
                    
        
    
