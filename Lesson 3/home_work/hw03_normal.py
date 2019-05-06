# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """ Возвращает последовательность ряда Фибоначи от n до m
    :param n:
    :param m:
    :return:
    """
    fib_part = [1, 1]
    for a in range(2, m):
        fib_part.append(fib_part[a - 1] + fib_part[a - 2])
    print(fib_part[n:m])

fibonacci(400, 505)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    ### Сортирует список origin_list по алгоритму Хоара ###
    if len(origin_list) <= 1:
        return
    left_list = []
    middle_list = []
    right_list = []

    zero = origin_list[0]

    for item in origin_list:
        if item < zero:
            left_list.append(item)
        elif item == zero:
            middle_list.append(item)
        else:
            right_list.append(item)

    sort_to_max(left_list)
    sort_to_max(right_list)

    i = 0
    for item in left_list + middle_list + right_list:
        origin_list[i] = item
        i += 1


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, lst):
    ### Фильрует последовательность lst по функции func ###
    buffer = []
    for item in lst:
        if func(item):
            buffer.append(item)
    return iter(buffer)
lst_num = [2, -500, 9, 17]
lst_str = ["One", "Two", "None", "24"]

def is_positive(num):
    return num > 0

def has_o(str):
    return 'o' in str.lower()

print(list(my_filter(is_positive, lst_num)))
print(list(my_filter(has_o, lst_str)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math
def is_parallelogram(A1, A2, A3, A4):
    ### Проверка лежат ли точки A1, A2, A3, A4 на вершинах параллелограмма ###
    d1 = math.hypot(A2[0] - A1[0],A2[1] - A1[1])
    d2 = math.hypot(A3[0] - A2[0],A3[1] - A2[1])
    d3 = math.hypot(A4[0] - A3[0],A4[1] - A3[1])
    d4 = math.hypot(A1[0] - A4[0],A1[1] - A4[1])

    if d1 == d3 and d2 == d4:
        return True
    else:
        return False

print(is_parallelogram([1,1],[3,1],[1,2],[3,2]))




