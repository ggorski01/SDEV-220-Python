# Program name: GGKilometers.py
# Author: Giovanna Gorski
# Date last updated: 06/19/2017
# Purpose: A simple function to accept the distance and compute the number of miles.  Output the number of kilometers and the number of miles.  

#Main function in which the value is inputed
def main():
   numberKilometers= int(input('Enter the number of kilometers as an integer: '))
   compute_miles(numberKilometers)
   
#The function compute_miles convert km to miles and display the output   
def compute_miles(number):
    numberMiles= (number* 0.6214)
    print('\n',number,'Kilometers is equal to', format(numberMiles,'.2f'), 'miles');
#Call the main function
main()