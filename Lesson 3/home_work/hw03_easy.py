# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    shift_position = 10 ** ndigits
    return int(number * shift_position + 0.5) / shift_position

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))




# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ### Вычисляет является ли номер билета счатливым ###
    digits = list(map(int, str(ticket_number)))
    if len(digits) % 2 != 0:
        return "Цифр в номере должно быть четное количество"
    else:
        middle = int(len(digits) / 2)
    first_half = digits[0:middle]
    second_half = digits[middle::1]
    if sum(first_half) == sum(second_half):
        return "Ура! Счастливый билет!!!\n Для получения порции счастья съешьте этот билет"
    else:
        return "Простите, этот билет не счастливый. Попробуйте в следующий раз"




print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(5646468495426846842968))
