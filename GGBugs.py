#Program name: GGBugs.py
#Author: Giovanna Gorski
#Date last updated: 6/12/2017
#Purpose: The program will colect the amount of bugs through five days, thus, calculate the total.
#Initiate the counter and the variable sum
sum=0
count=1 
#Loop that get the amount of bugs and sum the total of bugs
while count<=5:
  print('Day ',count)
  x= int(input('Enter the amount of bugs collected: '))
#calculate the total of bugs
  sum=sum+x
#increment the counter
  count=count+1

#Calculate the average of collected bugs
average=sum/count

#Display the calculate values
print('The total number of collected bugs at the end of five days is:',sum)
print('The average number of collected bugs at the end of five days is:',average)