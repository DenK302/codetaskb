def first_repeat(sym_list):
    list_index = []  # список для элементов и их индексов в получаемом списке
    for element in set(sym_list):  # удаление повторяющихся элементов из списка для того, чтобы найти индексы одинаковых
        list_index.append([[index for index, symbol in enumerate(sym_list) if symbol == element], element])
        # заполнение списка [[индексы], символ]
    diff_index = []  # список для хранения разницы между индексами одного элемента
    for index, symbol in list_index:
        if len(index) > 1:  # если индексов больше, чем один
            # с помощью разницы между индексами элемента можно найти те, которые повторяются ближе всего друг к другу
            diff_index.append([index[1] - index[0], str(symbol)])  # заполнение списка [разница индексов, символ]
    return min(diff_index)[1]  # возврат символа, полученного от минимальной разницы индексов


print(first_repeat(['a', 'b', 'c', 'c', 'b', 'a']))
