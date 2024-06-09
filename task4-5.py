'''
1. Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.

2. Дорабатываем задачу. Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить. 
В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
'''

import logging
import datetime
from sys import argv

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log_error.log', filemode='a', encoding='UTF-8', level=logging.ERROR,style="{" ,
                    format='{levelname} - {funcName} - {msg}')


WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

MONTHS = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

def some_func(data: str) -> datetime:
    try:
        cnt, weekday, month = data[1].split()
        try:
            cnt = int(cnt.split("-")[0])
            if (cnt>5):            
                logger.error(msg=f'{weekday} под №{cnt} не существует')
                raise ValueError()
        except ValueError as e:
            logger.error(msg=e)

        if (weekday in WEEKDAYS):
            weekday = WEEKDAYS[weekday]
        else:
            logger.error(msg=f'день недели "{weekday}" не существует или написан некорректно')
            raise ValueError()

        if (month in MONTHS):
            month = MONTHS[month]
        elif (int(month) in MONTHS.values()):
            month = int(month)
        else:
            logger.error(msg=f'"{month}" месяца не существует или написан некорректно')
            raise ValueError()
    except:
        logger.error(msg=f'Неверный формат ввода данных: {data}')
        cnt = 1
        month = datetime.datetime.today().month
        weekday = datetime.date(datetime.datetime.today().year, month, 1).weekday()


    first_weekday_month = datetime.date(datetime.datetime.today().year, month, 1).weekday()
    if (weekday-first_weekday_month)<0:
        find_day = cnt*7 - first_weekday_month + weekday + 1
    else:
        find_day = (cnt-1)*7 - first_weekday_month + weekday + 1

    try:
        return datetime.date(datetime.datetime.today().year, month, find_day)
    except ValueError as e:
        logger.error(msg=f"{datetime.datetime.today().year}-{month}-{find_day}: {e}")
        return "Дата не определена, смотрите логи"

print(some_func(argv))
