import sympy


def totient_phi(num):

    # phi(m) = (p1 - 1) * p1**(m1 - 1) * (p2 - 1) * p2**(m2 - 1) * (p3 - 1) * p3**(m3 - 1) * ...
    pfm = prime_factors_multi(num)
    result = 1
    for i in pfm:
        result *= (i[0] - 1) * i[0]**(i[1] - 1)
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


def prime_factors_multi(positive_int):

    result_buf = sympy.factorint(positive_int)

    result = [[result_buf_key, result_buf_value] for result_buf_key, result_buf_value in result_buf.items()]
    # for result_buf_key, result_buf_value in result_buf.items():
    #     result += [[result_buf_key, result_buf_value]]                      # += listに複数の要素を追加する
    return result
