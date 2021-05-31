from collections import Counter


def first_repeat(sym_list):
    for symbol, repeat_value in Counter(sym_list).items():
        if repeat_value > 1:
            return symbol


print(first_repeat(['a', 'b', 'c', 'c', 'a']))
