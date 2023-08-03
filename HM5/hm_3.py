# Создайте функцию генератор чисел Фибоначчи


def fibo(num):
    fibo_list = [0, 1]
    for i in range(num-1):
        fibo_list.append((fibo_list[i]) + (fibo_list[i+1]))
        temp_list = fibo_list.copy()
        fibo_list = temp_list
    return fibo_list

num = int(input("Введите число , для создания списка чисел Фибоначчи: "))
print(fibo(num))