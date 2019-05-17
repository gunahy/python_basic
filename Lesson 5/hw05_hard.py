# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    """ Вывод справки
    """
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    """ Создает директорию с указанным именем
    """
    target_dir = check_target(target_name)
    dir_path = os.path.join(os.getcwd(), target_dir)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(target_dir))
    except FileExistsError:
        print('директория {} уже существует'.format(target_dir))

def ping():
    print("pong")

def cp():
    """ Копирует указанный файл в текущую директорию
    """
    target_file = check_target(target_name)
    file_name = os.path.join(os.getcwd(), target_file)
    new_name = "copy_" + target_file
    copy_file = os.path.join(os.getcwd(), new_name)
    try:
        shutil.copy(file_name, copy_file)
        print("Файл {} скопирован".format(target_file))
    except shutil.SameFileError:
        print('Файл {} уже существует'.format(new_name))
    except OSError:
        print("Не удалось скопировать файл {}".format(target_file))
    

def rm():
    """ Удаляет указанный файл
    """
    target_file = check_target(target_name)
    if os.path.isfile(target_file):
        try:
            os.remove(os.path.join(os.getcwd(), target_file))
            print("Файл {} успешно удален".format(target_file))
        except OSError:
            print("Не удалось удалить файл {}".format(target_file))
    else:
        print("Вы указали директорию для удаления. Пожалуйста, укажите файл.")

def cd():
    """ Меняет рабочую директорию на указанную
    """
    target_dir = check_target(target_name)
    try:
        t_dir = os.path.abspath(target_dir)
        os.chdir(t_dir)
        print(os.getcwd)
    except:
        print("Неудалось перейти в папку {}".format(target_dir))


def ls():
    """ Выводит полный пут текущей директории
    """
    print(os.getcwd())

def check_target(target_name):
    """ Проверка наличия указанного параметра.
        Возвращает указанный параметр или None
    """
    if not target_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    else:
        return target_name

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    target_name = sys.argv[2]
except IndexError:
    target_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
