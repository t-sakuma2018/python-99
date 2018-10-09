import random


def rnd_select(data, the_number_to_extract):
    # data = [1, 2, 3], 3
    # result = [1, 3, 2]
    result = list(random.sample(data, the_number_to_extract))
    return result
