import random


def rnd_select(N, the_selected_numbers):
    # data = [1, 2, 3], 3
    # result = [1, 3, 2]
    list_0to9 = list(range(10))
    result = list(random.sample(list_0to9, N))
    result[-1] = the_selected_numbers
    return result
