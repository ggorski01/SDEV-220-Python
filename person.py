# Program name: person.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: This program contains the class for the program person_demo.py

#Class person
class Person:
    def __init__(self,name,address,telephone):
        self.__name=name
        self.__address=address
        self.__telephone=telephone
        
    #Set methods for the class person    
    def set_person_name(self,name):
        self.__name=name
    def set_person_address(self,address):
        self.__address=address
    def set_person_telephone(self,telephone):
        self.__telephone=telephone

    #Get methods fro the class person
    def get_person_name(self):
        return self.__name
    def get_person_address(self):
        return self.__address
    def get_person_telephone(self):
        return self.__telephone


    
class Customer(Person):
    def __init__(self,name,address,telephone,customer_number,mail_list):
        Person.__init__(self,name,address,telephone)
        self.__customer_number=customer_number
        #Set the mail list into a bolean if y therefore set to true if not set to False
        self.__mail_list= True if mail_list=='y' else False
        #self.__mail_list=mail_list
        
    #Set methods for the subclass customer    
    def set_customer_number(self,customer_number):
        self.__customer_number=customer_number
    def set_mail_list(self,mail_list):
        self.__mail_list=mail_list
        
    #Get methods for the subclass customer    
    def get_customer_number(self):
        return self.__customer_number
    def get_mail_list(self):
        return self.__mail_list
    
    #Function 
    def speak(self):
        return 'I am a Customer.'
