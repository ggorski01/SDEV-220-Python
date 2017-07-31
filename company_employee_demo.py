# Program name: company_employee_demo.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: Create an save informations about an employee using object orientation in Python

#Import the class Employee and ProductionWorker from the file company_employee.py
import company_employee


def main():
    print('Enter the following information for a production worker:')
    ename=input('Employee name: ')
    #Get the employee number
    enum=input('Employee Number (5 characters): ')
    #Validation loop for an employee number of 5 characters long only
    while len(enum)<5 or len(enum)>5:
        enum=input('Employee Number (exactly 5 characters): ')
    #Get the employee shift number
    shift=input('Shift Number: ')
    #Validation loop for the shift number be only 2 or 1
    while shift!='1' and shift!='2':
            shift=input('Shift Number (1 or 2 only): ')
    #Get the hourly pay rate        
    hrate=(float(input('Hourly rate: $')))
    #Create an object employee
    employee = company_employee.ProductionWorker(ename,enum,shift,hrate)

    #Display the attribute values in the employee object
    print('\nHere is the information for the production worker:')
    print('Employee name: ',employee.get_employee_name())
    print('Employee number: ',employee.get_employee_number())
    print('Shift number: ',employee.get_shift_num())
    print('Hourly rate: $',employee.get_pay_rates())
    
    
main()
wait=input('Press enter to exit...')
