import math


def goldbach_list(num_min, num_max, lower_limit=2):
    result = []
    for i in range(num_min, num_max + 1, 1):
        buf = goldbach(i, lower_limit)
        if not buf == []:
            buf = [i] + buf
            result += [buf]
        i += 1
    return result


def goldbach(num, lower_limit):
    result = []
    if lower_limit > 2:
        cnt = num // 13                                     # 13?
    else:
        cnt = num // 2

    if num - cnt <= 0:                                      # 素数候補がマイナスのとき
        return result

    if num > 4:
        for j in range(1, cnt):
            if is_prime(j) and is_prime(num - j):           # １　素数群か、
                result += [j, (num - j)]
                break
            j += 1

        if result == []:
            return result

        if result[0] <= lower_limit:                        # ２　50より大きいか。
            result = []
            return result
    return result


def is_prime(number):
    if number == 1:
        return False
    for p in range(2, int(math.sqrt(number) + 1)):
        if number % p == 0:
            return False
    return True
