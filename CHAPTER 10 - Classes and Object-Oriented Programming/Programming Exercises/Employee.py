class Employee:
    def __init__(self, name, ID, department, title):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__title = title
        
    def nameG(self):
        return self.__name
    
    def IDG(self):
        return self.__ID
    
    def departmentG(self):
        return self.__department
    
    def titleG(self):
        return self.__title
    
    def __str__(self): # Added cuz of C10PE7
        return f"ID: {self.__ID} \nName: {self.__name} \nDepartment: {self.__department} \nTitle: {self.__title}"