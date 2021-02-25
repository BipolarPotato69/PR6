import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

centimeter = float(input())

foot = centimeter / 30.48
inch = centimeter / 2.54

foot = round(foot, 2)
inch = round(inch, 2)

print(foot)
print(inch)
