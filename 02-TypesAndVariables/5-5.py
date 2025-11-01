product_price = float(input('enter product price :'))
discount = float(input('enter discount percentage % :'))
reduced_price = product_price * discount /100
price_with_discount = product_price - reduced_price
print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduced price: {reduced_price:.2f}')