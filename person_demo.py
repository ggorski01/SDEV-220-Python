# Program name: person.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: The program create and save information about customers

#Import the program person.py in which have the class Person and subclass Customer
import person

def main():
    
    print('Enter the following customer information:')
    #Get the attributs for customer
    c_name=input('Customer name: ')
    c_address=input('Address, City, State, Zip: ')
    c_tel=input('Telephone number: ')
    c_num=input('Customer number( 5 characters in length): ')
    #Validation for customer number be 5 characters in length
    while len(c_num)<5 or len(c_num)>5:
        print('Error')
        c_num=input('Customer number( 5 characters in length): ')
    mail=input('Do you want to be on the mailing list (y= yes, anything else=no: ')

    #Create the object Customer
    customer=person.Customer(c_name,c_address,c_tel,c_num,mail)


    #Display the attribute values in the Customer object
    print('\nHere is the information for the customer:')
    print('Customer name: ',customer.get_person_name())
    print('Address: ',customer.get_person_address())
    print('Telephone number: ',customer.get_customer_number())
    print('On mailing list: ',customer.get_mail_list())

    #Display the return from the function speak
    print(customer.speak())

main()

wait=('Press enter to exit...')
