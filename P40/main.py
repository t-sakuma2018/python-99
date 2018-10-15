
def goldbach(num):
    result = []

    if num <= 3:
        return result

    i = 2
    while i <= 5:
        if is_prime(i) and is_prime(num-i):
            result += [i, (num-i)]
            break
        i += 1

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
