# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    ### Возвращает последовательность ряда Фибоначи от n до m ###
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


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

