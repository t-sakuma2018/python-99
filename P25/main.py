import random


def random_permute(data):
    # data = [1, 2, 3, 4, 5])
    # result = [5, 1, 3, 4, 2]

    result = random.sample(data, len(data))
    return result
