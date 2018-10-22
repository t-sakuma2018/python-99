def encode_modified(data):    # data = [1, 2, 2, 3, 3, 3, 1, 1, 2, 3]
    # lists_buf                                  ----------------比較用の仮リスト
    lists_buf = [""]
    # lists                                      ----------------出力用リスト
    lists = [""]
    for a, b in enumerate(data):               # a=counter b=data[a]
        if lists_buf[-1] != b:
            if not len(lists_buf) == 1:
                lists.append([len(lists_buf), lists_buf[0]])
            else:
                lists.append(lists_buf[0])
            lists_buf = [""]
            lists_buf[0] = b
            continue
        else:
            lists_buf.append(b)
        a += 1
    if not lists_buf == [] and not len(lists_buf) == 1:
        lists.append([len(lists_buf), lists_buf[0]])
    else:
        lists.append(lists_buf[0])
    del lists[0]
    del lists[0]
    return lists
