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
    def wrapper(arg):
        func(arg)
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
    return address(a, b, c)


def address_json(addr_string):
    addr = json.loads(addr_string)
    a = addr['country']
    b = addr['city']
    c = addr['street']
    return address(a, b, c)


def address(country, city, street):
    """
    This func return address
    :param country: country
    :param city: city
    :param street: street
    :return: Full address that passed on delivery service
    """
    while True:
        for i in street:
            dom = rnd.randint(1, 20)
            kv = rnd.randint(1, 20)
            ac = re.search(r"^(?:[а-я(?: \-)?А-Я]+)$", i)
            if ac:
                yield print(f"Your destination address is: {country}, {city}, {i}, dom {dom}, kvartira {kv}")
            else:
                raise WrongStreet


if __name__ == '__main__':
    # address_json_file('addr.txt')
    # g = address_json('{"country": "Россия", "city": "Санкт-Петербург", "street": '
    #                  '["Вавиловых", "Энергетиков", "Чекистов"]}')
    # g = address('Россия', 'Санкт-Петербург', ["Вавиловых", "Энергетиков", "Чекистов"])
    # g = address(file='D:\\Serega\\!own\\PyCharm_profile\\ISAproj\\PY110-november-2018\\addr.txt')
    g = address_json_file('addr.txt')
    next(g)
    next(g)
    next(g)
    next(g)
    next(g)
    next(g)
    next(g)
