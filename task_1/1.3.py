#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10
while count > 0:
    n = int(input('Угадайте число от 1 до 1000. У вас осталось ' +str(count)+ ' попыток.'))
    if num == n:
        print('Вы угадали!')
        break
    elif num < n:
        print('Загаданное число меньше ' +str(n))
    elif num > n:
        print('Загаданное число больше ' + str(n))
    count -= 1
else:
    print('Попытки закончились. Вы не угадали. Загаданное число ' +str(num))