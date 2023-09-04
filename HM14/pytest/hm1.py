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
