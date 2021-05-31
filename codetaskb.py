def first_repeat(sym_list):
    elements = set(sym_list)
    list_index = [] #список для элементов и их индексов
    diff_index = [] #список
    for element in elements:
        list_index.append([[index for index, symbol in enumerate(sym_list) if symbol == element], element])
    for index, symbol in list_index:
        if len(index) > 1:
            diff_index.append([index[1] - index[0], str(symbol)])
    return min(diff_index)[1]


print(first_repeat(['a', 'c', 'b', 'b', 'c', 'a']))
