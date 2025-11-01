
#Write a program that reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT. Apply formatting with two decimal places. Sample result:

amount_string = input ('Enter amount: ')
amount = float(amount_string)
vat = amount * 0.23
print (f'Amount: {amount:.2f} VAT: {vat:.2f}')