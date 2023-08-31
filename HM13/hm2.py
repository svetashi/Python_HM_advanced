class CustomException(Exception):
    pass

class Fibonacci:
    def __init__(self, num: int):
        self.num = num
        if self.num.isalpha():
            raise CustomException("Ошибка: введите целое число!")

    def fibo(self):
        fibo_list = [0, 1]
        if int(self.num) > 50:
            raise CustomException('Число слишком большое')
        for i in range(int(self.num)-1):
            fibo_list.append((fibo_list[i]) + (fibo_list[i+1]))
            temp_list = fibo_list.copy()
            fibo_list = temp_list
        return fibo_list

fibo_num = input("Введите число , для создания списка чисел Фибоначчи: ")
fibo_class = Fibonacci(fibo_num)
print(fibo_class.fibo())