from sympy.combinatorics.graycode import GrayCode


def gray(num):
    gg = GrayCode(num)
    result = list(gg.generate_gray())
    return result
