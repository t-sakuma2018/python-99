def remove_at(data, remove_position):
    # data = ['a', 'b', 'c', 'd', 'e']         , 1
    # result =  [['b', 'c', 'd', 'e'], 'a']
    remove_position -= 1
    result_buf = ""
    result = []

    result_buf = data[remove_position]
    del data[remove_position]
    result = [data] + [result_buf]
    return result