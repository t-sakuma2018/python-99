def goldbach_list(num_min, num_max, lower_limit=2):
    # 引数が1, 2000, 50のとき→ｘ
    result = []

    num_list = range(num_min, num_max+1)

    for i in num_list:
        buf = []
        if is_even(i):
            buf = goldbach(i, lower_limit)
        if not buf == []:
            buf = [i] + buf  # [i, buf[0], buf[1]]
            result += [buf]
        i += 1
    return result


def goldbach(num, lower_limit):
    result = []

    if num <= 3:
        return result
    i = lower_limit

    loopy = range(i, 100)
    for j in loopy:

        if is_prime(j) and is_prime(num - j):
            result += [j, (num - j)]
            break
        j += 1

    return result


def is_prime(number):

    if number == 0:
        return False
    elif number == 1:
        return False

    for p in range(2, number):
        if number % p == 0:
            return False
    return True


def is_even(num):
    return num % 2 == 0
