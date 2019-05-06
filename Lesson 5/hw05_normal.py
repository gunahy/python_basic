# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import sys
import hw05_easy

sys.argv

def check_dir(dirname):
    """ Возвращает абсолютный путь к каталогу dirname,
        если он существует
    """
    if not dirname:
        print("Необходимо указать имя папки вторым параметром")
        menu()
        return
    dirpath = os.path.abspath(dirname)
    return dirpath if os.path.exists(dirpath) else None

def menu():
    """ Выводит меню в командной строке
    """
    print("Выберите действие:\n\
        \t 1-Сменить каталог\n\
        \t 2-Просмотреть содержимое текущей папки\n\
        \t 3-Удалить указанную папку\n\
        \t 4-Создать N папок в текущем каталоге\n")


def change_dir():
    """ Переходит в каталог указанный в параметре dirname
    """
    dirpath = check_dir(dirname)
    if dirpath:
        os.chdir(dirpath)
        print(f"Успешная смена каталога на {dirname}")
    else:
        print("Указанной папки не существует. Невозможно сменить каталог")

def list_dir():
    """ Выводит список каталогов в текущей папке
    """
    hw05_easy.dir_list()

def delete_dir():
    """ Удаляет папку с названием dirname
        в текущей папке
    """
    dirpath = check_dir(dirname)
    if dirpath:
        hw05_easy.del_dir(dirpath)
        print(f"Каталог {dirname} успешно удален")
    else:
        ("Невозможно удалить указанный каталог")


def create_dir():
    """ Создает n-ое количество папок в текущей директории.
        Количество n необходимо указывать 3 параметром
        ¯\_(ツ)_/¯ 
    """
    dirpath = check_dir(dirname)
    if not dirpath:
        hw05_easy.add_dir_n(dirname=dirname, n=count)
        print(f"Успешное создание каталогов {dirname} в количестве {count}")
    else:
        print("Невозможно создать указанный каталог")
    


do = {
    '1': change_dir,
    '2': list_dir,
    '3': delete_dir,
    '4': create_dir
}

try:
    dirname = sys.argv[2]
except IndexError:
    dirname = None
try:
    count = int(sys.argv[3])
except IndexError:
    count = 1
try:
    key = sys.argv[1]
except IndexError:
    key = None
    menu()

if key:
    print(count)
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ\n")
        menu()



    