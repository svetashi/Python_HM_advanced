# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

first_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for i in range(0, len(first_list)-1):
    if first_list.count(first_list[i]) > 1:
        new_list.append(first_list[i])
print(set(new_list))