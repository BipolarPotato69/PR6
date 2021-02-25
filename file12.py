import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

deposit = float(input("Deposit: "))
percent = int(input("Percent: "))
years = int(input("Years: "))

total = deposit * pow((1 + percent/100),years)
total = round(total, 2)

print(total)