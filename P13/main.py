def encode_direct(data):
    # data = [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]
    # result =  [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
    count = 1
    result = []
    for i in range(len(data)):
        try:
            if data[i] == data[i+1]:
                count += 1
            else:
                if count != 1:
                    result.append([count, data[i]])
                else:
                    result.append(data[i])
                count = 1
        except:                                         # "if num[i] == num[i+1]:" ←がエラーするとき
            if count != 1:
                result.append([count, data[i]])
            else:
                result.append(data[i])
            count = 1
    return result