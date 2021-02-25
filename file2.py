import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

#KROK2

name = "Kushnir " \
       "Alexander " \
       "Andreyevich"

message = "Hello my name is "
age = " I am 16 years old"

print(message + name + "." + age + ".")
