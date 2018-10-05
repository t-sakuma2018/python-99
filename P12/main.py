def decode(data):
    #data = [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
    # return [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5
    lists = []
    for a, b in enumerate(data):                                
        if type(b) == list:
            b_count = b[0]
            b_element = b[1]
            i = 0
            while i <= b_count-1:
                lists.append(b_element)
                i += 1
        else:
            lists.append(b)
    return(lists)     
         
    
