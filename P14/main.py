def duplicate(data):                                    # ダブらせる
    # data = [1, 2, 3, 3, 4])
    # result =  [1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
    count = 1
    result = []

    for i in range(len(data)):
        try:
            if data[i] == data[i+1]:
                count += 1
            else:
                if count != 1:
                    ii = 0
                    while ii <= count + 1:
                        result.append(data[i])
                        ii += 1
                    count = 1
                    continue
                else:
                    result.append(data[i])
                    result.append(data[i])
                    count = 1
        except:                                         # "if num[i] == num[i+1]:" ←がエラーするとき
            if count != 1:
                ii = 1
                while ii <= count:
                    result.append(data[i])
                    ii += 1
                count = 1
            else:
                result.append(data[i])
                result.append(data[i])
            count = 1
    return result