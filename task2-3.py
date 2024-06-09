'''
1. создать логирующий декоратор, чтобы он сохранял аргументы функции и результат её работы в файл: lesson9
'''

import logging
from typing import Callable
from functools import wraps

'''
2. На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
'''
def decor(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args  = (', args: ' + ', '.join(args)) if args else ''
        str_args  = (', args: ' + ', '.join(args)) if args else ''
        str_kwargs = (', kwargs: ' + ', '.join([f'{key}={value}' for key, value in kwargs.items()])) if kwargs else ''

        logger = logging.getLogger()
        logging.basicConfig(filename='log_decor.log', filemode='a', encoding='UTF-8', level=logging.INFO,style="{" ,
                        format='{msg}') 
        logger.info(msg=f'result: {result}{str_args}{str_kwargs}')
        return result
    return wrapper

'''
Доработаем задачу 2. Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
'''
def decor1(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args  = (', args: ' + ', '.join(args)) if args else ''
        str_args  = (', args: ' + ', '.join(args)) if args else ''
        str_kwargs = (', kwargs: ' + ', '.join([f'{key}={value}' for key, value in kwargs.items()])) if kwargs else ''
        logger = logging.getLogger()
        logging.basicConfig(filename='log_decor.log', filemode='a', encoding='UTF-8', level=logging.INFO,style="{" ,
                    format='{levelname} - {asctime:<20} - {funcName} - {msg}') 
        logger.info(msg=f'result: {result}{str_args}{str_kwargs}')
        return result
    return wrapper

#@decor
@decor1
def some_func(a: str, b: str):
    return a + '_' + b

some_func(a = 'aaa', b = 'ddd')




