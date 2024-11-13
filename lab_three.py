
day = int(input('Введите дату '))
month = int(input('Введите месяц '))
year = int(input('Введите год '))


if (1 <= day <= 31) and (1 <= month <= 12) and (1 <= year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month in ( 1,3 , 5 , 7 , 8,10 , 12):
            print(31 - day)
        if month == 2:
            print(29 - day)
        if month == 4 or month == 6 or month == 9 or month == 11:
            print(30 - day)
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print(31 - day)
        if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
            print(30 - day)
        if month == 2:
            print(28 - day)
else:
    print("Ошибка ввода данных")
