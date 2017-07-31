# Program name: GGChargeAccount.py
# Author: Giovanna Gorski
# Date last updated: 6/26/2017
# Purpose: The program have a main function that opens the text charge_accounts.txt file, reads the contents into a list, and closes the file. 

def main():
#Opens the file charge_accounts.txt to be read
        random_numbers = open('charge_accounts.txt', 'r')
#Create a list called L
        L=list()
#Found sinalizes if the account was font at the list or not
        found=0
#The for loop read each line in the document
        for line in random_numbers.readlines():
#At the end of each line of the document, there is a \n simbol at the end. The rstrip take care of removing the \n
                line = line.rstrip('\n')
#Append the read value to a position at the list
                L.append(line)	
#print(l) only to test if the values are been get from the file without the \n
#print(L)

#Ask to the user to input a 7 digit account number to be search in the list
        accountNumber = input('Enter a 7-digit account number to be searched: ')
#The for loop goes through the list, if found it sets the found to 1
        for i in L:
                if accountNumber==i:
                        found=1
#Checks if there is an account with the inputed number, if yes then display a positive message, or if not then display a negative message to the user
        if found==1:
                print('The account entered is valid')
        else:
                print('The account entered is invalid')
main()
wait=input('Press enter to exit')
