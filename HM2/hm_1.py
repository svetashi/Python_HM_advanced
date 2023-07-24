#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.



def hex_func(num:int):
    hex_num = ""
    convert = "0123456789ABCDEF"

    while num > 0:
        remainder = num % 16
        hex_num += convert[remainder]
        num //= 16
    
    return '0x'+''.join([i for i in reversed(hex_num)])


num = int(input("Введите число: "))
print(hex_func(num))
print(hex(num))



