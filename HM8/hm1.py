# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. В файле должен храниться список словарей, словарь описывает элемент внутри директории: имя, расширение, тип.
#  Если элемент - директория, то только тип и имя. Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

import json, os, pathlib

dir_elements = os.listdir()


def create_json(dir_elements):
    new_list = []
    for i in dir_elements:
        if os.path.isdir(i):
            file = i
            file_type = "directory"
            new_list.append({"name" : file, "extension" : file_type})
        else:
            file = pathlib.Path(i)
            filename = file.name.split('.')[0]
            extension = file.suffix
            file_type = "file"
            new_list.append({"name" : filename, "extension" : extension , "type" : file_type})
    return new_list


def write_in_file(new_list):
    with open("result.json", "w") as file:
        file.write(json.dumps(new_list, indent=2))

new_list = create_json(dir_elements)
write_in_file(new_list)
