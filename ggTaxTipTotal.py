#Program name: ggTaxTipTotal.py
#Author: Giovanna Gorski
#Date last updated: 6/11/2017
#Purpose: It calculates the total amount of meal purchased at a restaurant

#Get the charged number for the food
charged_food = float(input('Enter the charge food number: '))

#Calculate the amount of tip
amount_tip = charged_food*0.18

#Calculate the amount of sales tax
amount_sale_tax = charged_food*0.07

#Calculate the new total
total= amount_tip+amount_sale_tax+charged_food

#Display the the amounts

print('\nCharged food price: ',charged_food,'\n')
print('Amount of tip: ',amount_tip,'\n')
print('Amount of Sales taxes: ',amount_sale_tax,'\n')
print('Total amount: ',total)

#Hold the program open until the user's press the enter key
wait = input('\nPress enter to exit. ')
