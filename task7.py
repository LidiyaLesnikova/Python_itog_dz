'''
1. В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие 
атрибуты:
Фамилия (строка, не пустая) 
Имя (строка, не пустая) 
Отчество (строка, не пустая) 
Возраст (целое положительное число) 
Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). 
Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, 
если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). 
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID 
(по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при 
передаче неверных данных.

2. Добавьте логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки 
с передачей параметров.
'''

from sys import argv
import logging

logging.basicConfig(filename='log_list.log', filemode='a', encoding='UTF-8', level=logging.INFO,style="{" ,
                    format='{levelname}: {msg}')
logger = logging.getLogger(__name__)


class InvalidError(Exception):
    pass

class InvalidNameError(InvalidError):
    def __init__(self, *args: object) -> None:
        self.name = args[0]
    def __str__(self) -> str:
        message = f'Invalid name: {self.name}. Name should be a non-empty string.'
        logger.error(msg=message)
        return message
    
class InvalidAgeError(InvalidError):
    def __init__(self, *args: object) -> None:
        self.age = args[0]
    def __str__(self) -> str:
        message = f'Invalid age: {self.age}. Age should be a positive integer.'
        logger.error(msg=message)
        return message
    
class InvalidIdError(InvalidError):
    def __init__(self, *args: object) -> None:
        self.id = args[0]
    def __str__(self) -> str:
        message = f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'
        logger.error(msg=message)
        return message

class Person():
    lastname: str #Фамилия (строка, не пустая) 
    firstname: str #Имя (строка, не пустая) 
    patronymic: str #Отчество (строка, не пустая)
    _age: int #Возраст (целое положительное число)

    def __init__(self, lastname: str, firstname: str, patronymic: str, age: int) -> None:
        try:
            age = int(age)
        except ValueError as e:
            logger.error(msg=f'{e}: age is not int')
        if not lastname.replace(" ", "").isalpha():
            raise InvalidNameError(lastname)
        elif not firstname.replace(" ", "").isalpha():
            raise InvalidNameError(firstname)
        elif not patronymic.replace(" ", "").isalpha():
            raise InvalidNameError(patronymic)
        elif (not isinstance(age, int) or age<=0):
            raise InvalidAgeError(age)
        else:
            self.lastname = lastname.title()
            self.firstname = firstname.title()
            self.patronymic = patronymic.title()
            self._age = age

    def get_age(self):
        return self._age
        
    def birthday(self):
        self._age += 1

    def __str__(self) -> str:
        return f'{self.lastname} {self.firstname} {self.patronymic} - {self._age}'

class Employee(Person):
    def __init__(self, lastname, firstname, patronymic, age, id: int) -> None:
        super().__init__(lastname, firstname, patronymic, age)
        self._id = id

    def __setattr__(self, name, value) -> None:
        if (name=='id'):
            try:
                value = int(value)
            except ValueError as e:
                logger.error(msg=f'{e}: id is not int')
            if (not isinstance(value, int) or value<=0 or (value not in range(100000, 1000000))):
                raise InvalidIdError(value)
        object.__setattr__(self, name, value)
    
    def get_level(self):
        return sum([i for i in str(id)])//7
    
    def __str__(self) -> str:
        return f'{self.lastname} {self.firstname} {self.patronymic} - {self._age} (ID {self._id})'


#person = Employee("alice", "Smith", "Johnson", 25, 123456)

try:
    lastname = argv[1]
    firstname = argv[2]
    patronymic = argv[3]
    age = argv[4]
    id = argv[5]
    person = Employee(lastname, firstname, patronymic, age, id)
    print(person)
except IndexError:
     logger.error(msg=f'Неполная передача данных: {argv}')

