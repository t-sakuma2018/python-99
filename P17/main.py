def split(data, split_num):
    # data = [1, 2, 3, 4, 5] , 2
    # result =  [[1, 2], [3, 4, 5]])
    result_buf = []
    result = []
    split_num -= 1
    for data_cnt in range(len(data)):
        if split_num == -1:
            result.append([])
            result.append(data)
            break
        if split_num == len(data) - 1:
            result.append(data)
            result.append([])
            break
        if data_cnt == split_num:
            result_buf.append(data[data_cnt])
            result.append(result_buf)
            result_buf = []
        else:  # data_cnt != split_num
            result_buf.append(data[data_cnt])
    if result_buf != []:
        result.append(result_buf)
    return result
