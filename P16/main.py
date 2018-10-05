def drop(data, cnt):
    # data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 2
    # result =  ['a', 'c', 'e', 'g', 'i']
    result = []
    for data_cnt in range(len(data)):
        if (data_cnt + 1) % cnt != 0:
            result.append(data[data_cnt])
    return result
