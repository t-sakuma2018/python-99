import itertools


def combination(_k, n_data):
    result = []
    result_buf = list(itertools.combinations(n_data, _k))
    for i, name in enumerate(result_buf):
        result.append(list(name))
    return result








#
# def combination(_k, n_data):
#     result = []
#
#     integers = range(1, _k)
#
#     for n_data_buf, i in product(n_data, integers):
#         result.append([n_data_buf, i])
#     return result
# for i, iv in enumerate(n_data):
#     if _k == 2:
#         for j, jv in enumerate(n_data[i + 1:], start=(i + 1)):
#             result.append([iv, jv])
#     if _k == 3:
#         for j, jv in enumerate(n_data[i + 1:], start=(i + 1)):
#
#             for k, kv in enumerate(n_data[j + 1:], start=(j + 1)):
#                 result.append([iv, jv, kv])
#     if _k == 4:
#         for j, jv in enumerate(n_data[i + 1:], start=(i + 1)):
#             for k, kv in enumerate(n_data[j + 1:], start=(j + 1)):
#                 for l, lv in enumerate(n_data[k + 1:], start=(k + 1)):
#                     result.append([iv, jv, kv, lv])
#     if _k == 5:
#         for j, jv in enumerate(n_data[i + 1:], start=(i + 1)):
#             for k, kv in enumerate(n_data[j + 1:], start=(j + 1)):
#                 for l, lv in enumerate(n_data[k + 1:], start=(k + 1)):
#                     for m, mv in enumerate(n_data[l + 1:], start=(l + 1)):
#                         result.append([iv, jv, kv, lv, mv])