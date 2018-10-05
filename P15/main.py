def duplicate(data, cnt):                                    # ダブらせる
    # data = [1, 2, 3], 3
    # result =  [1, 1, 1, 2, 2, 2, 3, 3, 3]
    result = []
    i = 0

    for data_ in data:
        if cnt != 1:
            while i <= cnt - 1:
                result.append(data_)
                i += 1
            i = 0
        else:
            result.append(data_)
    return result