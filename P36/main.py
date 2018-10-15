import sympy


def prime_factors_multi(positive_int):
    result = []
    result_buf = sympy.factorint(positive_int)
    for result_buf_key, result_buf_value in result_buf.items():
        result += [[result_buf_key, result_buf_value]]                      # += listに複数の要素を追加する
    return result
