# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

simple = []
n = int(input('Ввидите число от 0 до 100000: '))
if (n < 0) or (n > 100000):
    print('Вы ввели некорректное число. Попробуйте еще раз')
for i in range(2, n+1):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        simple.append(i)
if n == 0 or n == 1:
    print('Число' +str(n)+ ' не является простым или составным')
elif n not in simple:
    print('Число ' +str(n)+ ' является составным')
elif n in simple:
    print('Число ' +str(n)+ ' является простым')