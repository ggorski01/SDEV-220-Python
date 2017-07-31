# Program name: company_employee.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: The following program contain the classes for the program company_employee_demo.py

#Class employee
class Employee:
    def __init__(self,name,number):
        self.__name=name
        self.__number=number
    #Set methods from the class employee
    def set_employee_name(self,name):
        self.__name=name
    def set_employee_number(self,number):
        self.__number=number
    #Get methods from the class employee
    def get_employee_name(self):
        return self.__name
    def get_employee_number(self):
        return self.__number
#Sub class ProductionWorker 
class ProductionWorker(Employee):
    #Sub class ProductionWorker have access to methods from the class Employee
    def __init__(self,name,number,shift_num,pay_rate):
        Employee.__init__(self,name,number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate
    #Set methods from the class ProductionWorker   
    def set_shift_num(self,shift_num):
        self.__shift_num = shift_num
    def set_pay_rate(self,pay_rate):
        self.__pay_rate = pay_rate
    #Get methods from the class ProductionWorker
    def get_shift_num(self):
        return self.__shift_num
    def get_pay_rates(self):
        return format(self.__pay_rate,',.2f')
