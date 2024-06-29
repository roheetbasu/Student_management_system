
import teacher
import json
import os 
import pathlib

with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
    json_content = json.load(file)

def authentication_for_teacher() -> bool:
    name_verify = input("Enter your name:")
    ID_verify = input("Enter your ID:")
    for record in json_content:
        if record["name"] == name_verify and record["ID"]  == ID_verify:
            return True
    return False