def slice(data, slice_start, slice_end):
    # data = [1, 2, 3, 4, 5], 1, 3
    # result =  [1, 2, 3]
    # result_buf = []
    result = []
    is_target_range = False
    for data_cnt in range(len(data)+1):
        if is_target_range:
            result.append(data_cnt)
            if data_cnt == slice_end:
                break
        else:
            if data_cnt == slice_start:
                is_target_range = True
                result.append(data_cnt)
            if data_cnt == slice_start == slice_end:
                break
    return result
