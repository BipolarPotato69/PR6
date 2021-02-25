import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

name = str(input("\nName: "))
pricePd = float(input("Price per dish: "))
quantity = float(input("Quantity: "))

price = pricePd * quantity

tips = price * 0.14
tax = price * 0.18
total = tax + tips + price

tips = round(tips, 2)
tax = round(tax, 2)
total = round(total, 2)

print("\nName----" + name)
print("Tips----" + str(tips))
print("Tax-----" + str(tax))
print("Total---" + str(total))
