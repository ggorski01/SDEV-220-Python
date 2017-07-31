# Program name: GGRandomNumberFile.py
# Author: Giovanna Gorski
# Date last updated: 6/26/2017
# Purpose: The program will create a file from a series of random numbers, and close the file.
#          The program will then open the same file for reading, count and total the random numbers 
#          in the file, display the total and the count 

#Import the library for randon number function
import random

def main():

#Create/open a file called ran_numbers
  random_numbers = open('randomNumbers.txt', 'w')
#Qty-numbers receives how many random numbers should be written into the file
  qty_numbers = int(input('Input how many random numbers should be written to the file: '))
#Call the function to create the file
  create_file(qty_numbers,random_numbers)
#Expection handler, it tries to open the randomNumbers.txt to read
  try:
    random_numbers = open('randomNumbers.txt', 'r')
    number = 0
    total = 0
    read_file(random_numbers,number,total)
    random_numbers.close()
#The except IOError detects if the randomNumber.txt encountered error or do not exist
  except IOError:
    print('An error occurred trying to read')
    print('the file ran_numbers.txt')
    wait=input('Press enter to exit')


 
#Create-file is a function that populate the file ran_numbers.txt
def create_file(qty_numbers,random_numbers):
#The for looping runs until the index is equal to qty_numbers
  for count in range (qty_numbers):
# The statement below attribute a random number to the variable number
    number = random.randint(1,500)
#The statement below write the randon number generated into the file ran_numbers.txt
    random_numbers.write(str(number)+ '\n')
#Close the file
  random_numbers.close()


#The read-file function read the file randomNumber.txt  
def read_file(random_numbers,number,total):
	print("List of the random numbers generated:")
#The for loop print each line of the file
	for line in random_numbers.readlines():
		print(line)
#The total sum the values that are in the file
		total = total+int(line)
		number +=1
#Display all the results
	print("The total of the numbers = "+str(total))
	print("The number of the random numbers read from the file = "+str(number))
	wait=input('Press enter to exit') 

main()
