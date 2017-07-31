# Program name: GGLotteryNumberList.py
# Author: Giovanna Gorski
# Date last updated: 6/26/2017
# Purpose: The lottery number list; it creates a list of random numbers from 0 to 99, therefore, place the numbers at a list

import random

def main():
#Create a list called L
  L=[]
#Counter variable
  i=0
 #Loop that will run the list until reach 6 in which is the numbers for the lottery
  while i<6:
 #Number will receive a random number created by the random function
    number=random.randint(0,99)
#The number created will be append at the list
    L.append(number)
#Counter will increase one to the next loop
    i+=1
    
#Display the numbers that are in the list one to each line
  for N in L:
    print (N)

main()
wait=input('Press enter to exit')
