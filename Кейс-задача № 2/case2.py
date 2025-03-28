from datetime import datetime

def is_leap_year(year):
    """
    Определяет, является ли год високосным.
    
    :param year: Год (целое число)
    :return: True, если год високосный, иначе False
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_weekday(day, month, year):
    """
    Получает день недели по дате.
    
    :param day: День (число)
    :param month: Месяц (число)
    :param year: Год (число)
    :return: Название дня недели на русском языке
    """
    date = datetime(year=int(year), month=int(month), day=int(day))
    weekday_number = date.weekday()
    weekdays = [
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье"
    ]
    return weekdays[weekday_number]

def calculate_age(birthdate):
    """
    Определяет возраст пользователя на основе даты рождения.
    
    :param birthdate: Дата рождения (строка в формате 'дд.мм.гггг')
    :return: Возраст в полных годах
    """
    birth_date = datetime.strptime(birthdate, '%d.%m.%Y')
    today = datetime.today()
    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def display_date_in_stars(birthdate):
    """
    Отображает дату рождения в формате звёздочек.
    
    :param birthdate: Дата рождения (строка в формате 'дд.мм.гггг')
    """
    # Словарь для представления каждой цифры звёздочками
    digit_to_stars = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["    *", "    *", "    *", "    *", "    *"],
        '2': [" *** ", "    *", " *** ", "*    ", " *** "],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", " *** ", "    *", "    *"],
        '5': [" *** ", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
        '7': [" *** ", "    *", "    *", "    *", "    *"],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " *** ", "    *", " *** "],
        ' ': ["     ", "     ", "     ", "     ", "     "]  # Для пробела
    }

    # Разбиваем дату на части
    day, month, year = birthdate.split('.')
    
    # Формируем вывод для каждой строки
    lines = ["", "", "", "", ""]
    
    # Обрабатываем каждую цифру в дате
    for part in [day, month, year]:
        for digit in part:
            stars = digit_to_stars[digit]
            for i in range(5):
                lines[i] += stars[i] + "  "  # Добавляем пробел между цифрами

    # Выводим результат
    for line in lines:
        print(line)

def get_birthdate():
    # Запрашиваем у пользователя день рождения
    day = input("Введите день вашего рождения (1-31): ")
    
    # Запрашиваем у пользователя месяц рождения
    month = input("Введите месяц вашего рождения (1-12): ")
    
    # Запрашиваем у пользователя год рождения
    year = input("Введите год вашего рождения (например, 1990): ")
    
    # Формируем дату рождения в формате 'дд.мм.гггг'
    birthdate = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
    
    # Получаем день недели
    weekday = get_weekday(day, month, year)
    
    # Проверяем, является ли год високосным
    leap_year = is_leap_year(int(year))
    
    # Вычисляем возраст
    age = calculate_age(birthdate)
    
    # Формируем и выводим информацию
    print(f"Ваша дата рождения: {birthdate}")
    print(f"Это был {weekday}.")
    
    if leap_year:
        print(f"{year} - високосный год.")
    else:
        print(f"{year} - невисокосный год.")
    
    print(f"Ваш возраст: {age} лет.")
    
    # Формируем дату рождения в формате 'дд.мм.гггг'
    birthdate = f"{day.zfill(2)}.{month.zfill(2)}.{year}"
    
    # Выводим дату рождения в звёздочках
    print("Ваша дата рождения в звёздочках:")
    display_date_in_stars(birthdate)

# Запускаем функцию
get_birthdate()
