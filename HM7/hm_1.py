# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes
import os
from pathlib import Path
import random
import string

print(__name__)

list_of_extensions = ['.txt', '.md', '.docx', '.odt']


def create_files(extension, min_name_len=6, max_name_len=30, min_bytes_size=256, max_bytes_size=4096, files_amount=2):
    for i in range(files_amount):
        letters = string.ascii_lowercase
        file_name = "".join(random.choice(letters) for j in range(random.randint(min_name_len,max_name_len)))
        file_to_create = str(file_name) + extension
        Path(file_to_create).touch()


        string_to_write = [random.randint(0,255) for _ in range(min_bytes_size, max_bytes_size)]
        bytes_string = bytes(string_to_write)
        with open(file_to_create, 'wb') as f:
            f.write(bytes_string)


if __name__=="__main__":
    for extension in list_of_extensions:
        create_files(extension, 6, 30, 256, 4096, 1) 