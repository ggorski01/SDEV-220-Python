#Program name: GGColor.py
#Author: Giovanna Gorski
#Date last updated: 6/12/2017
#Purpose: The program picks two primary colors,mix and you get a secondary color as a output.

#Get the primary colors
colorA= input('Enter the primary color 1: \n')
colorB= input('Enter the primary color 1: \n')

#logical test to match primary colors thus checking its results(secondary colors)
if colorA=='red' and colorB=='blue':
  print('When you mix red and blue, you get purple.')
elif colorA=='red' and colorB=='yellow':
  print('When you mix red and yellow, you get orange.')
elif colorA=='blue' and colorB=='yellow':
  print('When you mix blue and yellow, you get green.')
else:
  print('Error, renter the right color.')
  