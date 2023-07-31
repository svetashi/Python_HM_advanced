# Напишите функцию для транспонирования матрицы Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

arr = [[1,2,3],
       [4,5,6]]

def new_size(arr):
    new_size_arr = []
    for j in range(len(arr[0])):
        arr2 = []
        for i in range(len(arr)):
            arr2.append(0)
        new_size_arr.append(arr2)
    return new_size_arr

def fill_new_arr(new_size_arr):
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            new_size_arr[i][j] = arr[j][i]
    return new_size_arr

print(fill_new_arr(new_size(arr)))

 


