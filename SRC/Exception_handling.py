class NomatchingIDError(Exception):
    def __init__(self,ID):
        self.ID =ID
        self.message = f'{ID} is already used!!.Please use another one.'
        super().__init__(self.message)
        

class AuthenticationErrorforTeacher(Exception):
    def __init__(self,name,ID):
        self.ID =ID
        self.name = name
        self.message = f"{name} and {ID} don't match. Please try again!!"
        super().__init__(self.message)

class AuthenticationErrorforStudent(Exception):
    def __init__(self,name,roll):
        self.roll = roll
        self.name = name
        self.message = f"{name} and {roll} don't match. Please try again!!"
        super().__init__(self.message)
    
class NOmatchingRoll_NoError(Exception):
    def __init__(self,roll_no):
        self.roll_no = roll_no
        self.message = f"{roll_no} is already taken. please use another one!!"
        super().__init__(self.message)
        
class InvalidPhoneNoError(Exception):
    def __init__(self,phone_num):
        self.phone_num = phone_num
        self.message = f"{phone_num} is invalid.Please enter valid 10 digits!!"
        super().__init__(self.message)

class InvalidEmailError(Exception):
    def __init__(self,email):
        self.phone_num = email
        self.message = f"{email} is invalid. Please use @gmail.com to write email!!"
        super().__init__(self.message)

