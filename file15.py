import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

i = 0
while True:
    i += 1
    line = input("Data input number " + str(i) + "\n")
    if line == "end":
        break
