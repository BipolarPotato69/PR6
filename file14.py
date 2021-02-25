import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

P = float(input("Pressure in Pascal: "))
V = float(input("Volume in litres: "))
t = float(input("Temperature in Celsius: "))
R = 8.314

V = V / 1000
t = t + 273.3

n = round((P * V) / (R * t) , 2)

print(n)