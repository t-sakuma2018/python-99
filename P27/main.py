import itertools
import pdb # pdb.set_trace()
import pandas as pd
import numpy as np


def gp(groups_pattern, persons):
    result = []
    result_buf = []
    www = []
    end_flag = False
    cnt = len(persons)
    for ii, gg in enumerate(groups_pattern):
        if cnt == groups_pattern[-1]:  # 1通りのとき
            if end_flag:
                return result

            ncr_buf = list(itertools.combinations(persons, gg))
            del persons[:gg]
            print(str(cnt) + " 人から " + str(gg) + " 人を選ぶ組み合わせ(１通り）")
            for iii, name in enumerate(ncr_buf):
                www.append(list(name))
            result_buf.append(www[:])
            print(str(ii) + "   grouppata     総数→" + str(len(www)))
            del www[:]
            cnt = cnt - gg
            if len(result) == 0:
                result.append(result_buf[:])
            elif end_flag:
                return result
            else:
                for qqq in result_buf[0]:
                    if len(result_buf) == 1:
                        for name in result_buf:
                            result.append([name])
                    elif len(result_buf) >= 2:
                        for name, age in zip(result_buf[0], result_buf[1]):
                            result.append([name + age])
            del result_buf[:]
            result_buf.append("End")
        if cnt != groups_pattern[-1] and cnt >= groups_pattern[-1]:                            # 以上のとき
            ncr_buf = list(itertools.combinations(persons, gg))
            del persons[:gg]
            print(str(cnt) + " 人から " + str(gg) + " 人を選ぶ組み合わせ")
            for iii, name in enumerate(ncr_buf):
                www.append(list(name))
            result_buf.append(www[:])
            print(str(ii) + "   grouppata     総数→" + str(len(www)))
            del www[:]
            cnt = cnt - gg
        if result_buf[0] != "End" and result_buf != [] and cnt == groups_pattern[-1]:
            if len(groups_pattern) != 1:
                ncr_buf = list(itertools.combinations(persons, cnt))
                del persons[:cnt]
                print(str(cnt) + " 人から " + str(cnt) + " 人を選ぶ組み合わせ")  #  1鳥
                for iii, name in enumerate(ncr_buf):
                    www.append(list(name))
                result_buf.append(www[:])
                print(str(ii) + "   grouppata     総数→" + str(len(www)))
                del www[:]
                for qqq in result_buf[0]:
                    if len(result_buf) == 1:
                        for name in result_buf:
                            result.append([name])
                    elif len(result_buf) >= 2:
                        # ------------------------------------------------------------------------------------
                        # l_p = list(itertools.product(result_buf[0], result_buf[1]))
                        # end_flag = True
                        # for ooo in l_p:
                        #
                        #     result.append(ooo)
                        for name, age in zip(result_buf[0], result_buf[1]):
                            # print(result_buf[0])
                            # print(result_buf[1])
                            result.append([name, age])
                            end_flag = True
                        # ------------------------------------------------------------------------------------
    # print(result)
    print("----------------------------------------------")
    return result


def group3(persons):
    # 引数 = ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida']
    # 戻り値　= 組み合わせ list
    groups_pattern = [2, 3, 4]
    result = gp(groups_pattern, persons)
    print("結果は")
    print(len(result))
    print("です")
    return result


def group(groups_pattern, persons):
    # 引数 = [9], ['aldo', 'beat', 'carla', 'david', 'evi', 'flip', 'gary', 'hugo', 'ida']
    # 戻り値　= list
    # [5, 4]のとき126
    groups_pattern.sort()
    result = gp(groups_pattern, persons)
    print("結果は")
    print(len(result))
    print("です")
    return result
