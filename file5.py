import datetime

name1 = 'Alexander Kushnir'

def printTimeStamp(name1):
    print('\nАвтор програми:' + name1)
    print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp(name1)

document = """---------------------------------------------------------------------
            Рахунок-фактура № ______ вiд ________
---------------------------------------------------------------------
ПОСТАЧАЛЬНИК:                       ПЛАТНИК: ЧП Іванов Іван Іванович
Управлiння Iнженерного захисту
територiї мiста та розвитку
узбережжя ОМР Код ЭДРПОУ
24760454 Р/р №: 35420014002262
МФО 828011 в ГУДКУ в Одеськiй областi
---------------------------------------------------------------------
Пiдстава:
---------------------------------------------------------------------
| № |    Найменнування товару     | Од.вим. | Кiльк. | Цiна  | Сума |
|   | Узгодження проектної        |         |        |       |      |
|   | документацiї нового         |  услуг  | 1.00   | 0.00  | 0.00 |
|   | будiвництва за адресою      |         |        |       |      |
|   | м.Одеса,вул.Iванова,896     |         |        |       |      |
---------------------------------------------------------------------
                                              Всього без ПДВ | 0.00 |
                                                         ПДВ | 0.00 |
                                           Всього сума з ПДВ |      |
                                                             --------
"""
print(document)