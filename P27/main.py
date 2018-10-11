import itertools


def group3(persons):
    groups_pattern = [2, 3, 4]
    result = []
    # aaaa = persons
    dictaa = {"count": len(persons)}
    for ii, gg in enumerate(groups_pattern):
        if dictaa["count"] != groups_pattern[-1]:
            # aaaa -= gg
            dictaa["count"] = dictaa["count"] - gg
            # print(dictaa["count"])
            result_buf = list(itertools.combinations(persons, gg))

            for iii, name in enumerate(result_buf):
                result.append(list(name))
            print(len(result))

    # print(result)
    # print(len(result))
    return result

