# Program name: recursive_lines.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: Draw the images with asteristics. An example of recursion

#Function recursive
def power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * power(x, y - 1)

def main():
    #Get the base number
    base=int(input('Enter the base number: '))
    #Get the exponent number
    expo=int(input('Enter the exponent (power) as a non-negative integer: '))
    #Validation loop to the exponent number be positive
    while expo<0:
        expo=int(input('Enter the exponent (power) as a non-negative integer: '))

    #Call recursive function
    print(base,'raised to the power of ',expo,'is ',power(base,expo))

main()
wait=input('Press enter to exit...')
