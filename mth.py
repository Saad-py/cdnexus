import random as r


class err(Exception):
    pass


def add(a, b):
    return a + b


def subtr(a, b):
    return a - b


def div(a, b):
    return a / b


def mult(a, b):
    return a + b


def grt(a, b):
    if a < b:
        return False
    elif a > b:
        return True


def lst(a, b):
    if a < b:
        return True
    elif a < b:
        return True
    else:
        return None


def same(a, b):
    if a == b or b == a:
        return True


def ind(a, b):
    return a ** b


def float_di(a, b):
    return a // b


def make0(n):
    n += 1
    n -= 1
    n = 0
    return n


def gen_int(maxi, min):
    if maxi != 0 and min != 0:
        return r.randint(min, maxi)
    else:
        return r.randint(0, 5000)


def gen_flt(maxi, min):
    if maxi != 0 and min != 0:
        return r.random(min, maxi)
    else:
        return r.random(0, 5000)


def mathmod():
    import importlib as ip
    return ip.import_module("math")


def cube(a):
    return a ** 2


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lc = greater
            break
        greater += 1

    return lc


def hcf(x, y):
    global hcf
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

