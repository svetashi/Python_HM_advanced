# Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами, которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.
import json

def cache_deco(func):
    def wrapper(a, b):
        a = str(a)
        b = str(b)
        try:
            with open(f'{func.__name__}.json', 'r') as cache:
                print("Reading cache...")
                new_dict = json.loads(cache.read())
        except Exception as e:
            new_dict = {}
        if func.__name__ in new_dict:
            if a in new_dict[func.__name__]:
                if b in new_dict[func.__name__][a]:
                    result = new_dict[func.__name__][a][b]
                    print(f"Got result for {a} and {b} from cache: {result}!")
                    print()
                    return result
                
        print(f'Result not in cache, calculating for {a} and {b}...')
        result = func(int(a), int(b))
        new_dict.setdefault(func.__name__, {})
        new_dict[func.__name__].setdefault(a, {})
        new_dict[func.__name__][a][b] = result
        print(f"Calculated result is {result}!")
        with open(f'{func.__name__}.json', 'w') as cache:
            print("Writing results to cache...")
            cache.write(json.dumps(new_dict, indent=4))
        print()
        return result
    return wrapper

@cache_deco
def sum(a, b):
    c = a + b
    return c

# Not in cache initially
sum(1, 2)

sum(1, 3)

sum(2, 3)


# Should be from cache
sum(1, 2)