import json
import os 
import pathlib

with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
    json_content_teacher = json.load(file)

with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
    json_content_students = json.load(file)

def authentication_for_teacher(name,ID) -> bool:
    name_verify = name
    ID_verify = int(ID)
    for record in json_content_teacher:
        if record["name"] == name_verify and record["ID"]  == ID_verify:
            return True
    return False

def authentication_for_students(name,roll) -> bool:
    name_verify = name
    Roll_verify = int(roll)
    for record in json_content_students:
        if record["name"] == name_verify and record["roll_no"]  == Roll_verify:
            return True
    return False