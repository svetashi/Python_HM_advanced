# Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}
import ast

def reverse_kwargs(**words):
    new_dict = {}
    for key, value in words.items():
        new_dict[value] = key
    return new_dict
        



print(reverse_kwargs(rev=True, acc="YES", stroka=4))

