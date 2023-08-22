# Создайте функцию генератор чисел Фибоначчи

class Fibonacci:
    def __init__(self, num: int):
        self.num = num

    def fibo(self):
        fibo_list = [0, 1]
        for i in range(self.num-1):
            fibo_list.append((fibo_list[i]) + (fibo_list[i+1]))
            temp_list = fibo_list.copy()
            fibo_list = temp_list
        return fibo_list

fibo_num = int(input("Введите число , для создания списка чисел Фибоначчи: "))
fibo_class = Fibonacci(fibo_num)
print(fibo_class.fibo())