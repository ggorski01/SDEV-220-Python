#Program name: ggSalesPrediction.py
#Author: Giovanna Gorski
#Date last updated: 6/11/2017
#Purpose: Input the projected amount of sales and the program will display the profit that will be made from this amount

#Get the projected amount of sales
projected_amount = float(input('Enter the projected amound of sales: '))

#Calculate the annual profit
annual_profit = projected_amount*0.23

#Display calculated value for annual profit
print('The annual profit will be: ',annual_profit)

#Hold the program open until the user's press the enter key
wait = input('Press enter to exit. ')


