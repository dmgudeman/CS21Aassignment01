
# -----------------------------------------------------------------------------
# Name:        tax
# Purpose:     sales tax calculator
#
# Author:      David Gudeman
# Date:        06/10/2015
# -----------------------------------------------------------------------------

"""
Sales tax calculator assuming a 8.75% sales tax rate

Prompt the user for the cost of the item.
Print the sales tax amount and the total cost.
"""

TAX_RATE = 8.75/100         # the sales tax rate constant: 8.75%

user_input = input('Please enter the price of your item in $: ')
cost = float(user_input)  # convert the input string to a number

tax = TAX_RATE * cost     # calculate the tax amount
tax = round(tax, 2)       # round tax to two decimals

print('Sales Tax: $', tax, sep='')   # suppress the space separator

total = cost + tax        # the total cost of the item
total = round(total, 2)   # round total to two decimals

print('Total Cost: $', total, sep='') # suppress the space separator
