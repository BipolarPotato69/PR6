import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

#KROK1

multistringName ="""\nKushnir
Alexander
Andreevich\n"""

print(multistringName)




