# Program name: recursive_lines.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: Draw the images with asteristics. An example of recursion

#Function recursive
def draw_lines(n):
    if (n > 1):
        #While draw_line is true, the function call it self
        draw_lines(n-1)
    #Therefore print the line with asteristics
    print ('*' * n)

def main():
    #Get the number of lines
    line=int(input('Enter the number of lines to be drawn: '))
    #Validation loop to the number be between 1 and 10
    while line<1 or line>10:
        line=int(input('Enter the number of lines to be drawn: '))
    #Call recursive function
    draw_lines(line)
main()
wait=input('Press enter to exit...')
