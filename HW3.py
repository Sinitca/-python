# 1.Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# def get_list(n, frst, last):  
    # return [randint(frst, last) for i in range(n)] 

# def sum_odd_position(mylist): 
    # return sum(mylist[1::2]) 

# n = 10
# frst = 1
# last = 10

# mylist = get_list(n, frst, last)
# print(mylist)
# print(sum_odd_position(mylist))

# 2.Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#  Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# from random import randint
# import math

# def get_numbers(n, frst, last):
#     return [randint(frst, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 9
# frst = 1
# last = 10

# mylist = get_numbers(n, frst, last)
# print(mylist)
# print(mult_pairs(mylist))


# # Второй способ:

# def pairs_mult(numbers):
#     results = []
#     while len(numbers) > 1:
#         results.append(numbers[0]*numbers[-1])
#         del numbers[0] 
#         del numbers[-1] 
#     if len(numbers) ==1: results.append(numbers[0]**2)       
#     return results

# print(pairs_mult(mylist))


# 3.Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
#минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform

# def get_real_nums (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]

# def find_diff(mynums):
#     nums = [round(x - int(x), 2) for x in (mynums)]
#     return max(nums) - min(nums)

# n = 5
# frst = 1
# last = 10
# mynums = get_real_nums(n, frst, last)

# print (mynums)
# print(find_diff(mynums))

