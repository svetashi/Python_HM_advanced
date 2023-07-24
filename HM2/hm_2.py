#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import fractions
import math

num = input("Введите дробь: a/b ")  #3/5
num2 = input("Введите дробь: c/d ") #1/2

div1 = [int(a) for a in num.split("/")]
div2 = [int(a) for a in num2.split("/")]

def sum_div(a, b):
    ok = a[1] * b[1]

    amul = ok / a[1]

    atop = a[0] * amul

    bmul = ok / b[1]

    btop = b[0] * bmul

    topres = atop + btop
    botres = ok

    return f"{topres}/{botres}"

def mul_div(a, b):
    res_top = a[0] * b[0]
    res_bot = a[1] * b[1]

    return f"{res_top}/{res_bot}"


print(sum_div(div1, div2), mul_div(div1, div2))



f = fractions.Fraction(num)
d = fractions.Fraction(num2)
print(f+d, f*d)