def insert_at(insert_position, target_element, data):
    # data = 0, -1, [1, 2, 3, 4]
    # result =  [-1, 1, 2, 3, 4]
    data.insert(insert_position, target_element)
    result = data
    return result
