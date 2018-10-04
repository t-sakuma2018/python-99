def compress(data):
    lists = []
    for a, b in enumerate(data):    #a=カウンタ b=data[a]
        if a == 0:                  #初回のみlistsにdata[0]を代入
            lists.append(b)
        if lists[-1] != b:          #listsに最後に追加された要素とカレント要素を比較
            lists.append(b)
        a +=1
    return(lists)      