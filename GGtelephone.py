# Program name: GGtelephone.py
# Author: Giovanna Gorski
# Date last updated: 07/10/2017
# Purpose: The program have a main function that translate alphabet telephone numbers such as 555-GET-FOOD to only numbers. (EXAM 2)

def main():
#Get the alphabet telephone number from the user
    phoneNumber = input('Enter the number in the format of 555-XXX-XXXX\n')
#Variable in which will receive the phone number converted
    newPhoneNumber=''
#For loop that runs through every character that the user inputed.
    for char in phoneNumber:
#Validations, if the char A, B or C, thus, the variable that contains the converted number will concatenate the new value.
        if char == 'A' or char == 'B' or char == 'C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'
#Converted phone number will append the new char.
        newPhoneNumber = newPhoneNumber+char
#Display the results
    print(phoneNumber,'IS THE SAME NUMBER AS ',newPhoneNumber)
main()
wait=input('\nPress enter to exit...')
