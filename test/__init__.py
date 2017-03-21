import timeit
from enum import Enum


def make_dict():
    dct = {}
    for i in range(15):
        dct['d{}'.format(i)] = i
    return dct

class En(Enum):
    d1 = {"a":1}
    d2 ={"a":2}
    d3 ={"a":3}
    d4 = {"a":4}
    d5 = {"a": 5}
    d6 = {"a": 6}
    d7 = {"a": 7}
    d8 = {"a": 8}
    d9 = {"a": 9}
    d10 = {"a": 10}
    d11 = {"a": 11}
    d12 = {"a": 12}
    d13 = {"a": 13}
    d14 = {"a": 14}
    d15 = {"a": 15}


def dict_get(_dict, ky):
    return _dict[ky]

dct = make_dict()

def enum_get(val):
    for ky in En:
        if ky.value["a"]==val:
            return ky
    return None

if __name__ == "__main__":
    t = timeit.Timer("dict_get(dct,'d14')", setup="from __main__ import dict_get, dct")
    print(t.timeit(10))
    t = timeit.Timer("dict_get(dct,'d1')",
                     setup="from __main__ import dict_get, dct")
    print(t.timeit(10))

    t = timeit.Timer("enum_get(15)",setup="from __main__ import En,enum_get")
    print(t.timeit(10))
    # timeit.timeit(stmt=s, number=100000)
