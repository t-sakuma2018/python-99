from operator import itemgetter


def lsort(InList):
    # 引数 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]
    # 戻り値 = [['o'], ['d', 'e'], ['d', 'e'], ['m', 'n'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['i', 'j', 'k', 'l']]

    result_buf = [[i, len(i)] for i in InList]          # リスト内包表記　[[['d', 'e'],2], [['f', 'g', 'h'],3]]
    result_buf.sort(key=itemgetter(1))                  # 要素(1)でソート
    result = [j[0] for j in result_buf]                 # リスト内包表記　[['d', 'e'], ['f', 'g', 'h']]
    return result
