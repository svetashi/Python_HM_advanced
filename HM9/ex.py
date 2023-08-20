import time

# def deco(test): 
#     def wrapper(sec):
#         t = time.localtime()
#         current_time = time.strftime("%H:%M:%S", t)
#         print(current_time)
#         test(sec)
#         t = time.localtime()
#         current_time = time.strftime("%H:%M:%S", t)
#         print(current_time)
#         return sec
#     return wrapper

# @deco
# def test(sec):
#     print(f"Sleeping for {sec} seconds")
#     time.sleep(sec)
#     return sec

# test(4)
import random, string, os

def deco(func):
    def wrapper(name, length):
        with open (name+".log", "w") as l:
            pass
        func(name,length)
        os.remove(name+".log")
        return True
    return wrapper


@deco
def func(name, length):
    with open (name, "a") as f:
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        time.sleep(5)
        f.write(result_str + "\n")


func("text.txt", 8)