applePrice = 0.50

userName = input('Please enter your name:')
print('Hello',userName)

print('Apples cost ${price:.2f} each.'.format(price = applePrice))

appleQuan = int(input('How many apples would you like?:'))
print('Thank you, {name}, for purchasing {quantity:,} apples at ${price:.2f} each. \
Your total is ${total:.2f}.'.format(quantity = appleQuan, name = userName, price = applePrice, total = appleQuan*applePrice))