import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

qThings = int(input("Things:"))
qThingies = int(input("Thingies:"))

mThings = qThings * 75
mThingies = qThingies * 112

total = mThings + mThingies

print(str(total)+"grams")