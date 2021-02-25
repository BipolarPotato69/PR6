import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

quantity = int(input("Quantity:"))

price = quantity * 8.50
discount = quantity * 8.50 * 0.6
total = price - discount

price = "%.2f" % price
discount = "%.2f" % discount
total = "%.2f" % total

formatted_price = "{:>166}".format(price)
formatted_discount = "{:>166}".format(discount)
formatted_total = "{:>166}".format(total)

print(formatted_price)
print(formatted_discount)
print(formatted_total)