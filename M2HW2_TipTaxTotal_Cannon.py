
# CTI-110 
# M2HW2 - Tip Tax Total 
# Lisa Cannon
# 10SEP17
# Program to calculate tip for a meal.
foodCost = int(input('What did your food cost? '))
tipAmount = foodCost * .18
salesTax = foodCost * .07
totalCost = foodCost + tipAmount + salesTax
# Calculations for tax, tip, and total.
print('Sales Tax: ', format(salesTax, ',.2f'))
print('18% Tip: ', format(tipAmount, ',.2f'))
print('Total Cost: ', format(totalCost, ',.2f'))
