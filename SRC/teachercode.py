import json
import os.path
import pathlib
import Data_validate 
import Exception_handling 
import authentication
# path = os.getcwd()
# filename = "TeacherData.json"
# filepath = os.path.join(path,filename)
# print(filepath)
class Teacher():
    def __init__(self,name,email,phone_num,address,subject,ID) -> None:
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.address = address
        self.subject = subject
        self.ID = ID      
    
    @classmethod
    def create_Teacher(cls,name,email,phone_num,address,subject,ID)->None:
        return cls(name,email,phone_num,address,subject,ID)

    def LoadFirstData(self) -> None:
        Dict1 = {
                "name" : self.name,
                "email" : self.email,
                "phone_num" : self.phone_num,
                "address" : self.address,
                "subject" : self.subject,
                "ID" : self.ID  
            }    
        file_path = 'D:\\Python\\Project1\\Data_storage\\TeacherData.json'
        if os.path.exists(file_path):
            with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
                json_content = json.load(file)
                json_content.append(Dict1)
            with open(r"D:\Python\Project1\Data_storage\TeacherData.json","w") as file:
                json.dump(json_content,file,indent=4)        
        else:
            List1 = []
            with open(r"D:\Python\Project1\Data_storage\TeacherData.json","w") as file:
                List1.append(Dict1)
                json.dump(List1,file,indent=4)    
                
def Validate_email(email) -> bool:
    email = email.split('@')
    if email[-1] == 'gmail.com':
        return True
    return False


def Validate_num(num) -> bool:
    if len(num) == 10:
        return True
    return False

def Entry4Teacher() -> None:
    print(f"Enter the following details---------")
    name = input("Name:")
    while True:
        email = input("Email:")
        try:
            if Validate_email(email):
                break
            else:
                raise Exception_handling.InvalidEmailError(email)
        except Exception_handling.InvalidEmailError as e:
            print(e.message)
    while True:
        phone_num = input("Phone Number:")
        try:
            if  Validate_num(phone_num):
                break
            else:
                raise Exception_handling.InvalidPhoneNoError(phone_num)
        except Exception_handling.InvalidPhoneNoError as e:
            print(e.message)

    
    address = input("Address:")
    subject = input("Subject:")
    while True:
        ID = int(input("ID:"))
        try:
            if Data_validate.Data_validationTeacher(ID):
                break
            else:
                raise Exception_handling.NomatchingIDError(ID)
        except Exception_handling.NomatchingIDError as e:
            print(e.message)
            
    Teacher1 = Teacher.create_Teacher(name,email,phone_num,address,subject,ID)
    Teacher1.LoadFirstData()
    
    
def Display_all() -> None:
    with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
        json_content = json.load(file)
            
    for i in json_content:
        print(f'Name:{i["name"]}')
        print(f'Email:{i["email"]}')
        print(f'Address:{i["address"]}')
            
def Delete() -> None:
    with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
        json_content = json.load(file)
            
    DeleteName = input("Enter name to Deleted Data:")
    DeleteID = int(input("Enter Id:"))
    try:
        if authentication.authentication_for_teacher(DeleteName,DeleteID):
            pass
        else:
            raise Exception_handling.AuthenticationErrorforTeacher(DeleteName,DeleteID)
    except Exception_handling.AuthenticationErrorforTeacher as e:
            print(e.message)
            exit()
    list1 = []
    for record in json_content:
        dict1 = {}
        if record["name"] == DeleteName and record["ID"] == DeleteID:
            continue
        for k,v in record.items():
            dict1[k] = v
        list1.append(dict1)
        
    with open(r"D:\Python\Project1\Data_storage\TeacherData.json","w") as file:
        json.dump(list1,file,indent = 4)

def search(name,ID) -> None:
    with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
        json_content = json.load(file)
            
    s_name = name
    s_ID = ID
    for record in json_content:
        if record["name"] == s_name and record["ID"] == s_ID:
            for k,v in record.items():
                print(f"{k} = {v}")

