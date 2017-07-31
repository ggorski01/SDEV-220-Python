# Program name: GGCelsiusToFah.py 
# Author: Giovanna Gorski
# Date last updated: 06/19/2017
# Purpose:A program that displays a table of the Celsius temperatures 1 through 20 and their Fahrenheit equivalents

#Set the variables that are going to hold the temperature to zero
tempC=0
tempF=0

#Display preformated output
print(' Temperature table 1-20 degrees\n','Degree Celsius|','|Degree Fahrenheit')

#Loop that shows the temperatures until temperature Celsius be equal or less than 20 degrees
while tempC<=20:
#Formula that converts degree celsius in degree Fahrenheit
  tempF=(9/5)*tempC + 32
#Display results
  print('    ',format(tempC,'.2f'),'          ',format(tempF,'.2f'))
#Tempc is the degree celsius and a counter variable
  tempC+=1

#Hold the program open until the user's press the enter key
wait = input('\nPress enter to exit. ')