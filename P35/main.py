import sympy


def prime_factors(positive_int):
    result = []
    result_buf = sympy.factorint(positive_int)
    for result_buf_key, result_buf_cnt in result_buf.items():
        while result_buf_cnt >= 1:
            result.append(result_buf_key)
            result_buf_cnt -= 1
    print(result)
    return result
