# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys


def user_check_data(user_date):
    int_user_date = [int(x) for x in user_date]

    day_valid = False
    month_valid = False
    year_valid = False

    if int_user_date[0] <= 31 and int_user_date[0] >= 1:
        day_valid= True
    else:
        print("ERROR day")
        day_valid= False
    
    if int_user_date[1] <= 12 and int_user_date[1] > 1:
        month_valid= True
    else:
        print("ERROR mounth")
        month_valid= False

    if int_user_date[2]>= 1 and int_user_date[2] <= 9999:
        year_valid= True
    else:
        print("ERROR year")
        year_valid= False


    if day_valid & month_valid & year_valid:
        return True
    else:
        return False

def _check_year(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("високосный")
        return True
    else:
        print("не високосный")
        return False
    


if __name__ == "__main__":
    if len(sys.argv)>1:
        _, date = sys.argv[0:2]
        _check_year(date.split('.')[-1])
    else:
        user_date = input("Введите дату в формате DD.MM.YYYY: ").split(".")
        date_valid = user_check_data(user_date)
        print("Date correct" if date_valid else "Date incorrect")