#Program name: GGSumOfNumbers.py
#Author: Giovanna Gorski
#Date last updated: 6/12/2017
#Purpose:The program will get positive numbers until a negative number inputed, thus, the sum of the positive numbers will display

#Initiate the variable responsible to validate the loop
x=99
#initiate the variable responsible to keep the sum of the positive values
sum=0

#loop
while x>0:
  x=int(input('Enter a positive value or a negative to signal the ende of the series: '))
#If the input number is positive, thus, add to the variable that keep the sum of the positive values
  if x>0:
    sum=sum+x
#if there's positive values, display it.
if sum>0: 
  print('The sum of the positive numbers are:',sum)
#In case of the first number be inputed by the user is a negative number, the program will end.