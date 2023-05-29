# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

n = int(input('Введите число: '))
i = n
base = 16
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
result = ''
while i > 0:
    result = digits[i % base] + result
    i //= base
print(result)
print(hex(n))

