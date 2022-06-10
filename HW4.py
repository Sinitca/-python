# 1. Написать программу, преобразовавыющую десятичные числа 
# в двоичные
# n = int(input('Введите число: '))

# def conv_dec_to_bin(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]
# print(conv_dec_to_bin(n))

# 2. Зaдать число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов
# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

# 3. Задать строку из набора чисел. Написать программу, которая покажет 
# большее и меньшее число. В качестве символа - разделителя использовать пробел
# string = '34 45 89 4 9 5 2 1'

# def convert_to_int(str):
#     return[int(x) for x in str.split()]

# str_list = convert_to_int(string)
# print(min(str_list), max(str_list))

# 4. Задать два целых числа. Написать программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел
# from math import lcm

# a = 4
# b = 9

# def get_lcm(a, b):
#     return lcm(a, b)

# print(get_lcm(a, b))

