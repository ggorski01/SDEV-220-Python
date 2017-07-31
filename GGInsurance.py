# Program name: GGInsurance.py
# Author: Giovanna Gorski
# Date last updated: 06/19/2017
# Purpose: The program displays the minimum amount of insurance that is needed after a user input the the replacement cost of a building

#Main function in which the value is inputed
def main():
   replacementCost= int(input('Enter the replacement cost of the building: '))
   compute_insurance (replacementCost)
   
#The function compute_insurance calculate 80% over the replacement cost 
def compute_insurance(number):
    insuranceNeeded= (number* 80)/100
#Displays the amount of insurance needed for the building
    print('Amount of insurance is $',format(insuranceNeeded,',.2f'));
    
#Call the main function
main()