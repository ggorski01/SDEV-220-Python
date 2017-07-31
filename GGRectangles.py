#Program name: GGRectangles.py
#Author: Giovanna Gorski
#Date last updated: 6/12/2017
#Purpose: Input the width and length of two rectangles. The program should tell the user which rectangle has greater area


#Get the widths and lengths of the two rectangles
lengthA= int(input('Enter the length of the rectangle 1: \n'))
widthA= int(input('Enter the width of the rectangle 1: \n'))

lengthB= int(input('Enter the length of the rectangle 2: \n'))
widthB= int(input('Enter the width of the rectangle 2: \n'))

#Calculate area of each rectangle separatly
areaA= lengthA * widthA
areaB= lengthB * widthB

# Logical test to see which rectangle have greater area or if the two has same area
if areaA == areaB:
	print('Areas are equals')
elif areaA > areaB:
	print('The rectangle 1 has greater area.\n')
else:
	print('The rectangle 2 has greater area.\n')
	
#Hold the program open until the user's press the enter key
wait = input('Press enter to exit. ')