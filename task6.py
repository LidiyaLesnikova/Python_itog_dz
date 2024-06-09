'''
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

from sys import argv
import os
import logging
from collections import namedtuple

logging.basicConfig(filename='file_list.txt', filemode='w', encoding='UTF-8', level=logging.INFO,style="{" ,
                    format='{levelname}: {msg}')
logger = logging.getLogger(__name__)

def info_dir(path: str):
    if not os.path.exists(path):
        logger.error(msg=f'Директория {path} не доступна.')
        raise ValueError("Указан неверный путь (подробности в логах)")

    FileInfo = namedtuple("FileInfo", ['name', 'extension', 'type', 'directory'], rename=False, defaults=None, module=None)
    for files in os.walk(path):
        for file in files[1]:
            ntuple = FileInfo(file, '', 'Directory', files[0])
            logger.info(msg=ntuple)
        for file in files[2]:
            file_split = file.rsplit('.', 1)
            ntuple = FileInfo(file_split[0], file_split[1] if len(file_split)>1 else "", 'File', files[0])
            logger.info(msg=ntuple)

try:
    info_dir(argv[1])
except IndexError as e:
    logger.critical(msg=f'{e}: не введен путь')