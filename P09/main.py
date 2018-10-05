def pack(data):
    #data = [1, 2, 2, 3, 3, 3, 1, 1, 2, 3]

    #lists_buf                                  ----------------比較用の仮リスト
    lists_buf = [""]
    #lists                                      ----------------出力用リスト
    lists = [""]
    for a, b in enumerate(data):                                #a=counter b=data[a]

        #print("-----------------------------------------")
        #print("1 a = ")
        #print(a)
        #print("2 b = ")
        #print(b)
        #print("3 lists_buf[-1] = ")
        #print(lists_buf[-1])
        #print("-------------------")
        
        if lists_buf[-1] != b:          
            #lists_bufの最後に追加された要素とカレント要素を比較　==>違うとき
            #lists_bufの要素群をlistsに移動し、lists_bufにはカレント要素を入れる


            #print("4 lenLists = " + str(len(lists)))
            #print("5 strLists = ")
            #print(lists)
            #print("6 strLists_buf = ")
            #print(lists_buf)
            lists.append(lists_buf)     
            lists_buf = [""]
            lists_buf[0] = b
            continue
        else:
            #おなじとき
            lists_buf.append(b)

        a +=1
    if lists_buf != []:
        
        lists.append(lists_buf)
        lists_buf = []

    #出力リストに不要な要素が発生してしまう為、力技で解決    
    del lists[0]
    del lists[0]

    #print("OWARI-------------")
    return(lists)      