#Prompt the user to enter a product description
userItem = input('Please enter the product you wish to purchase: ')

#Prompt the user to enter the quantity being purchased
quantity = int(input(f'Please enter the quantity of {userItem}(s) you wish to purchase: '))

#Prompt the user to enter the regular price of the product
regPrice = float(input(f'Please enter the price of the {userItem}(s) before tax: '))

#All products over 19.99 are 15% off.
if regPrice > 19.99 and regPrice < 39.99:
    origPrice = regPrice
    regPrice = regPrice - (regPrice * 0.15)
    print(f'The {userItem}(s) are 15% off. That means the new price per item is {regPrice:,.2f}')
    #Display the total amount saved by the customer
    print(f'You saved ${((origPrice - regPrice) * quantity):,.2f}')
elif regPrice > 39.99:
    origPrice = regPrice
    regPrice = regPrice - (regPrice * 0.25)
    print(f'The {userItem}(s) are 25% off. That means the new price per item is {regPrice:,.2f}')
    #Display the total amount saved by the customer
    print(f'You saved ${((origPrice - regPrice) * quantity):,.2f}')

#Calculate the sales tax on the total purchase
priceAftTax = float((regPrice * quantity) + ((regPrice * quantity) * 0.065))

#Display the total amount due by the customer
print(f'---- Your reciept ----')
print(f'Sales Tax (6.5%): {((regPrice * quantity) * 0.065):,.2f}')
print(f'{quantity} {userItem}(s) @ {regPrice:,.2f} each')
print(f'Total: ${priceAftTax:,.2f}')