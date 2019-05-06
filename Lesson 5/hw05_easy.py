# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

def get_root(rootdir):
    """ Если корневой каталог не указан, 
        возвращает текущий
    """
    return rootdir if rootdir else os.getcwd()

def add_dir_n(rootdir='', dirname='dir_', n=1):
    """ Создает в корне директории rootdir
        каталоги с именем dirname + i, 
        где i - число из списка от 1 до n + 1 
    """
    rootdir = get_root(rootdir)
    os.chdir(rootdir)
    for i in range(1, n+1):
        try:
            os.mkdir(str(dirname) + str(i))
        except FileExistsError:
            print(f"Каталог {dirname} уже существует")
            continue

def del_dir_n(rootdir='', dirname='dir_', n=1):
    """ Удаляет в корне директории rootdir
        каталоги с именем dirname + i, 
        где i - число из списка от 1 до n + 1 
    """
    rootdir = get_root(rootdir)
    for i in range(1, n+1):
        del_dir(os.path.join(rootdir, dirname + str(i)))

def del_dir(absroot):
    """ Удаляет папку по абсолютному пути
    """
    if os.path.exists(absroot):
        os.rmdir(absroot)
    else:
        print(f"Каталог {absroot} не существует")

    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_list():
    """ Отображает каталоги в текущей директории
    """
    lstdir = []
    for d in os.listdir():
        if not os.path.isfile(d):
            lstdir.append(d)
    print(lstdir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file(rootdir=''):
    """ Копирует текущий файл скрипта в директорию rootdir,
        Если директория не указана, копирует в текущую 
        добавляя к имени файла '_copy'
    """
    rootdir = get_root(rootdir)
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    ext = os.path.splitext(os.path.basename(__file__))[1]
    if rootdir == os.getcwd():
        shutil.copyfile(__file__,  file_name + '_copy' + ext)
    else:
        shutil.copyfile(__file__, os.path.join(rootdir, os.path.basename(__file__)))



