def f(i):
    print('zaczynamy z liczba', i)
    if i in [0, 1]:
        result = 1
    else:
        result = f(i - 1) + f(i - 2)
        print('koncze zi liczba', i)
        return result


def mul(i, j):
    if j < 0:
        return -i + mul(i, j + 1)
    if j == 0:
        return 0
    if j == 1:
        return i
    else:
        return i + mul(i, j - 1)


def sign(i):
    if i > 0:
        return 1
    else:
        if i == 0:
            return 0
        else:
            return -1


def sign2(i):
    if i > 0:
        return 0
    if i == 0:
        return 0
    return -1


def ola():
    print('jestem ola')
    return None


def s(i):
    print('zaczynam z liczba', i)
    if i == 0:
        result = 1
    else:
        result = 1 * s(i - 1)
    print('koncze z liczba', i)
    return result

# print(f(5))
# print (s(5))
# print(mul(0, 7))
# ola()
