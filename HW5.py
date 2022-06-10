# 35
# задана натуральная степень k
# сформировать случайным образом список коэффициентов
# (от 0 до 100) многочлена 
# записать в файл многочлен степени k 

# пример k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)

# 35
# создать файл
# записать в созданный файл N натуральные  числа 
# для выполнения условия А[i] - 1 = A[i - 1] найти недостающее число  в списке

file = open('Num.txt', 'w')
file.write('2 ')
file.write('4 ')
file.write('8 ')
file.write('16 ')
file.write('64 ')
file.write('128 ')
file.close()

# file = open('Num.txt', 'r')
# print(file.read())

# with open ('Num.txt', 'r') as test: 
#     for line in test:
#       z = line.split()
#     for num in z:
        
def get_data_from_file(nums):
    data = open(nums, 'r')
    dlist = data.read() + ' '
    dlist = list(map(int, dlist.split()))
    data.close()
    return dlist

def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1

fnums = 'Num.txt'
nums_list = get_data_from_file(fnums)


def get_full_nums(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            nums.insert(i+1, nums[i] + 1)
    return nums

nums = get_data_from_file(fnums)

print(get_full_nums(nums_list))


# massiv = []
# massiv = datas.split(',')

# massiv = list(map(int, massiv))
# print(massiv)


# 43
# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# num = [1, 2, 2, 3, 3, 3, 4, 5,5]
# def get_unique_num(num):
#     list_of_unique_num = []
#     unique_num =set(num)

#     for num in unique_num:
#         list_of_unique_num.append(num)

#     return list_of_unique_num

# print(get_unique_num(num))

