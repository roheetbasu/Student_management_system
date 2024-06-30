import json

with open(r"D:\Python\Project1\Data_storage\TeacherData.json","r") as file:
    json_contentteacher = json.load(file)

with open(r"D:\Python\Project1\Data_storage\studentsData.json","r") as file:
    json_contentstudents = json.load(file)
    
def Data_validationTeacher(ID:int)-> bool:
    for record in json_contentteacher:
        if record["ID"] == int(ID):
            return False
        return True


def Data_validationStudent(roll_no:int)-> bool:
    for record in json_contentstudents:
        if record["roll_no"] == int(roll_no):
            return False
        return True


