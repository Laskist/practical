# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

# вводим строки
a, b = map(int, input('Введите строку вида a/b: ').split('/'))
c, d = map(int, input('Введите строку вида c/d: ').split('/'))


# вычисление наименьшего общего кратного
def calculate_lcm(b, d):
    if b > d:
        greater = b
    else:
        greater = d
    while (True):
        if ((greater % b == 0) and (greater % d == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


lcm = calculate_lcm(b, d)


def calculate_numbers():
    # вычисляем дополнительный множитель
    multiplier_1 = lcm // b
    multiplier_2 = lcm // d
    # добаляем доп множитель к числителю
    numerator_1 = a * multiplier_1
    numerator_2 = c * multiplier_2
    numerator = numerator_1 + numerator_2
    return numerator


numerator = calculate_numbers()
divider_list = []

# Вычисляем, можно ли сократить дробь. Ищем наименьшее из числителя и знаменателя.
# Перебираем все числа до наименьшего включительно, деля числитель и знаменатель.
# Получаем список с возможными числами на которое можно сократить, переворачиваем его.
def calculate_pov(lcm, numerator):
    if lcm > numerator:
        smaller = numerator
    else:
        smaller = lcm
    for i in range(1, smaller + 1):
        if lcm % i == 0:
            if numerator % i == 0:
                divider_list.append(i)
    divider_list.reverse()
    return divider_list

# Запрашиваем получаемый список, из него берем только первую позицию
divider_list = calculate_pov(lcm, numerator)
divider = int(divider_list[-len(divider_list)])

# результат в числителе
def numerator_result():
    if numerator % divider == 0:
        numerator_result = int(numerator / divider)
    else:
        numerator_result = numerator
    return numerator_result
# Результат в знаменателе
def lcm_result():
    if lcm % divider == 0:
        lcm_result = int(lcm / divider)
    else:
        lcm_result = lcm
    return lcm_result

print('Результат сложения дробей: ' + str(numerator_result()) + "/" + str(lcm_result()))

dev_list = []
pon = a * c
pod = b * d
# Вычисляем, можно ли сократить полученную. Ищем значения, на которые будет делиться
# и числитель, и знаменатель.Перебираем все числа до наименьшего включительно.
# Получаем список с возможными числами на которое можно сократить, переворачиваем его.
def calculate_dev(pon, pod):
    if pon > pod:
        smaller = pod
    else:
        smaller = pon
    for i in range(1, smaller + 1):
        if pon % i == 0:
            if pod % i == 0:
                dev_list.append(i)
    dev_list.reverse()
    return dev_list

# Запрашиваем получаемый список, из него берем только первую позицию
dev_list = calculate_dev(pon, pod)
dev = int(dev_list[-len(dev_list)])

# сокращенный результат умножения в числителе
def pon_result():
    if pon % dev == 0:
        pon_result = int(pon / dev)
    else:
        pon_result = pon
    return pon_result

# сокращенный результат умножения в знаменателе
def pod_result():
    if pod % dev == 0:
        pod_result = int(pod / dev)
    else:
        pod_result = pod
    return pod_result
print('Результат умножения дробей: ' +str(pon_result())+"/"+str(pod_result()))


# проверка
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print('Проверка сложения дробей: ' +str(f1 + f2))
print('Проверка умножения дробей: ' +str(f1 * f2))
