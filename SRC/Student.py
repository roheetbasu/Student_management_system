import json
import os
import pathlib
 
class Student():
    def __init__(self,name:str,email:str,phone_num:int,address:str,roll_no:int,marks:dict) -> None:
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.address = address
        self.roll_no = roll_no
        self.marks = marks
        self.status = None
        self.percentage = None
        self.Highest = None
        self.Lowest = None
        self.Rank = None
        
    @classmethod
    def create_student(cls,name:str,email:str,phone_num:int,address:str,roll_no:int,marks:dict)->None:
        return cls(name,email,phone_num,address,roll_no,marks)
    
    def Pass_fail_deter(self):
        for v in self.marks.values():
            self.status = "Pass"
            if v < 40:
                self.status = "Fail"
                break
    
    def Highest_Lowest_score(self) -> None:
        self.Highest = max(self.marks.values())
        self.Lowest = min(self.marks.values())
    
    def Percentage_calc(self) -> None:
        self.percentage = sum(self.marks.values())/len(self.marks.values())
        if self.status == 'Fail':
            self.percentage = None
      
    
    def LoadFirstData(self) -> None:
        Dict1 = {
                "name" : self.name,
                "email" : self.email,
                "phone_num" : self.phone_num,
                "address" : self.address,
                "roll_no" : self.roll_no,
                "marks" : self.marks,
                "status" : self.status,
                "percentage" : self.percentage,
                "Highest" : self.Highest,
                "Lowest" : self.Lowest,
            }    
        file_path = 'D:\\Python\\Project1\\Data_storage\\studentsData.json'
        if os.path.exists(file_path):
            with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
                json_content = json.load(file)
                json_content.append(Dict1)
            with open(r"D:\Python\Project1\Data_storage\studentsData.json","w") as file:
                json.dump(json_content,file,indent=4)        
        else:
            List1 = []
            with open(r"D:\Python\Project1\Data_storage\studentsData.json","w") as file:
                List1.append(Dict1)
                json.dump(List1,file,indent=4) 

def Validate_email(email) -> bool:
    if '@' in email:
        return True
    return False 

def Validate_num(num) -> bool:
    if len(num) == 10:
        return True
    return False 
    
def Rank_cal() -> None:
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
        json_content = json.load(file)
    List1 = []
    for v in range(len(json_content)):
        List1.append(json_content[v]["percentage"])
    List1.sort(reverse=True)
    print(List1)
    for i,idx in enumerate(List1):
        for records in json_content:
            if records["percentage"] == idx:
                records['Rank'] = i+1
                if records['status'] == 'Fail':
                    records['Rank'] = None
                    
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","w") as file:
        json.dump(json_content,file,indent=4)
            
                    
def Entry4students() -> None:
    print(f"Enter the following details---------")
    name = input("Name:")
    email = input("Email:")
    phone_num = int(input("Phone Number:"))
    address = input("Address:")
    roll_no = int(input("Roll No:"))
    print("Enter Marks-------")
    marks = {
        "Maths" : int(input("Maths:")),
        "English" : int(input("English:")),
        "Science" : int(input("Science:")),
        "Computer" : int(input("Computer:"))
    }
    while Validate_email():
        print(f'Please enter a valid email-----------------')
        email = input("Email:")
    while Validate_num(phone_num):
        print(f'Please enter a valid phone number(10 digits)------------')
        phone_num = int(input("Phone Number:"))
    Student1 = Student.create_student(name,email,phone_num,address,roll_no,marks)
    Student1.Percentage_calc()
    Student1.Pass_fail_deter()
    Student1.Highest_Lowest_score()
    Student1.LoadFirstData()
    Rank_cal()
    
      
def Display_all() -> None:
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
        json_content = json.load(file)
            
    for i in json_content:
        print(f'Name:{i["name"]}')
        print(f'Email:{i["email"]}')
        print(f'Email:{i["address"]}')
            
def Delete() -> None:
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
        json_content = json.load(file)
            
    DeleteName = input("Enter name to Deleted Data:")
    list1 = []
    for record in json_content:
        dict1 = {}
        if record["name"] == DeleteName:
            continue
        for k,v in record.items():
            dict1[k] = v
        list1.append(dict1)
        
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","w") as file:
        json.dump(list1,file,indent = 4)

def search() -> None:
    with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
        json_content = json.load(file)
            
    s_name = input("Enter name to search:")
    for record in json_content:
        dict1 = {}
        if record["name"] == s_name:
            for k,v in record.items():
                print(f"{k} = {v}")
                


