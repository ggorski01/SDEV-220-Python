# Program name: employee.py
# Author: Giovanna Gorski
# Date last updated: 07/11/2017
# Purpose: The program create a class called Employee in which will be used in the file
#          employee_manager.py


# The Employee class holds Employee information.

class Employee:
    # The __init__ method initializes the attributes.
    def __init__(self, name, idNumber, department,jobTitle):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__jobTitle = jobTitle
    # The set methods sets the attributes.
    def set_name(self, name):
        self.__name = name

    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber

    def set_department(self, department):
        self.__department = department
        
    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle
    
    # The get methods returns the attributes.
    def get_name(self):
        return self.__name

    def get_idNumber(self):
        return self.__idNumber

    def get_department(self):
        return self.__department
		
    def get_jobTitle(self):
        return self.__jobTitle

    # The __str__ method returns the object's state as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__idNumber + \
               "\nDepartment: " + self.__department+\
	       "\nJob Title: " + self.__jobTitle
    
