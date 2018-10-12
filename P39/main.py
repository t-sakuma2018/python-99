import sympy


def prime_numbers(num_1, num_2):

    buf = [num_1, num_2]
    buf.sort()

    result = list(sympy.primerange(buf[0], buf[1]))
    return result
