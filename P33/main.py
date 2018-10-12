import math


def is_coprime(number_1, number_2):

    if gcd(number_1, number_2) == 1:
        return True
    return False


def gcd(number_1, number_2):
    result = math.gcd(number_1, number_2)
    return result