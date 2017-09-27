# CTI 110
# Lisa Cannon
# M3HW1 Software Sales
# 24SEP17

def main():
#Program to calculate discounts for bulk orders

# number of copies need for discounts
    discountTen = 10
    discountTwenty = 20
    discountThirty = 50
    discountForty = 100

# Calculation for Suntotal
    quantity = int(input('Number of copies purchased: '))
    nondiscountPrice = (quantity * 99)
    print ('Subtotal: $',format(nondiscountPrice, ',.2f'))

# Calculations for discounts
    discountOne = nondiscountPrice * .10
    discountTwo = nondiscountPrice * .20
    discountThree = nondiscountPrice * .30
    discountFour = nondiscountPrice * .40

    if quantity < discountTen:
        print ('Discount: $ 0.00')
        print ('Total: $',format(nondiscountPrice, ',.2f'))

    elif quantity < discountTwenty:
         print ('Discount: $',format(discountOne, ',.2f'))
         print ('Total: $',format(nondiscountPrice - discountOne, ',.2f'))

    elif quantity < discountThirty:
         print ('Discount: $',format(discountTwo, ',.2f'))
         print ('Total: $',format(nondiscountPrice - discountTwo, ',.2f'))

    elif quantity > discountForty:
         print ('Discount: $',format(discountThree, ',.2f'))
         print ('Total: $',format(nondiscountPrice - discountThree, ',.2f'))     

    else:
         print ('Discount: $',format(discountFour, ',.2f'))
         print ('Total: $',format(nondiscountPrice - discountFour, ',.2f'))


main()


