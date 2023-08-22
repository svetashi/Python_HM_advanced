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


class Serealisation:
    def __init__(self, dir_elements: list):
        self.dir_elements = dir_elements

    def create_json(self):
        new_list = []
        for i in self.dir_elements:
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

    def write_in_file(self, new_list):
        with open("result.json", "w") as file:
            file.write(json.dumps(new_list, indent=2))

dir_elements = os.listdir()
ser_class = Serealisation(dir_elements)

new_list = ser_class.create_json()

ser_class.write_in_file(new_list)
