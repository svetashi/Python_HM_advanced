# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt

# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


import os 
from pathlib import Path

def way(path):
    p = os.path.abspath(path)
    return p, Path(p).name.split('.')[0], Path(p).suffix



cortege = way('file.txt')
print(cortege)
path, filename, extension = cortege
print(f"Path: {path}")
print(f"Filename: {filename}")
print(f"Extension: {extension}")
