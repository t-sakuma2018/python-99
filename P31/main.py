def is_prime(number):

    if number == 0:
        return False
    elif number == 1:
        return False

    for p in range(2, number):
        if number % p == 0:
            # print(str(number) + ' is composite.')
            return False
    # print(str(number) + ' is PRIME!!')

    return True
