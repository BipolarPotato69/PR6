import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

C = int(input())
K = C + 273.3
F = (C * 1.8) + 32
print(K)
print(F)
