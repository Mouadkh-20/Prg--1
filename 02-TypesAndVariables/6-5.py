###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'Phone number entered: {phone[0:4]}-{phone[4:7]}-{phone[7:10]}')