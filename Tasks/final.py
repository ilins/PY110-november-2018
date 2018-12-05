"""
Module generates addresses
"""
import re
import random as rnd
import json


class AddressError(Exception):
    pass


class WrongStreet(AddressError):
    pass


def decorator(func):
    """
    This one is for debug purpose
    :return:
    """
    def wrapper(*args, **kwargs):
        template = 'test'
        if kwargs:
            for i in kwargs.values():
                if template == i:
                    return f"Вызов функции с параметрами: {kwargs}. Имя вызванной функции: {func.__name__}"
        elif args:
            if template in args:
                return f"Вызов функции с параметрами: {args}. Имя вызванной функции: {func.__name__}"
        else:
            res = func(*args, **kwargs)
            return res
    return wrapper


def address_json_file(file=""):
    """
    Import from file json format
    :return:
    """
    with open(file, 'r') as f:
        addr = json.load(f)
    a = addr['country']
    b = addr['city']
    c = addr['street']
    return a, b, c


def address_json(addr_string):
    addr = json.loads(addr_string)
    a = addr['country']
    b = addr['city']
    c = addr['street']
    return a, b, c


@decorator
def address(nfile="", nstring=""):
    """
    This func generates addresses
    :param nfile: input file
    :param nstring: input string
    :return: addresses
    """
    street = []
    if nstring:
        data = address_json(nstring)
        country = data[0]
        city = data[1]
        street = data[-1]
    if nfile:
        data = address_json_file(nfile)
        country = data[0]
        city = data[1]
        street = data[-1]
    while True:
        for i in street:
            dom = rnd.randint(1, 20)
            kv = rnd.randint(1, 20)
            ac = re.search(r"^(?:[а-я(?: \-)А-Я]+)$", i)
            if ac:
                yield print(f"Your destination address is: {country}, {city}, {i}, dom {dom}, kvartira {kv}")
            else:
                raise WrongStreet


if __name__ == '__main__':
    # address_json_file('addr.txt')
    # g = address_json('{"country": "Россия", "city": "Санкт-Петербург", "street": '
    #                  '["Вавиловых", "Энергетиков", "Чекистов"]}')
    # g = address('Россия', 'Санкт-Петербург', ["Вавиловых", "Энергетиков", "Чекистов"])
    # g = address(nfile='addr.txt')
    # g = address(nstring='{"country": "Россия", "city": "Санкт-Петербург", "street":'
    #                     '["Вавиловых", "Энергетиков", "Чекистов"]}')
    # g = address(nstring='test')
    g = address(nfile='test')
    print(g)
    # g = address_json_file('addr.txt')
    # next(g)
    # next(g)
    # next(g)
    # next(g)
    # next(g)
    # next(g)
    # next(g)
