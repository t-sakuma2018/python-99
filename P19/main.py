def rotate(data, rotate_position):
    # data = [1, 2, 3, 4, 5, 6], 3
    # result =  [4, 5, 6, 1, 2, 3]
    result = data[rotate_position:] + data[:rotate_position]
    return result