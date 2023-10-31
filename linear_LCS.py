from suffix_trees import STree


def linear_longest_common_substring(x, y):
    # Создаем обобщенное суффиксное дерево из двух строк
    stree = STree.STree([x, y])

    # Находим наибольшую общую подстроку
    lcs = stree.lcs()
    # print(lcs)
    if not lcs:
        return None

    start_index_x = x.find(lcs)
    end_index_x = start_index_x + len(lcs)
    start_index_y = y.find(lcs)
    end_index_y = start_index_y + len(lcs)

    return (start_index_x, end_index_x, start_index_y, end_index_y)

'''
# Пример использования
x = "umgeschaut"
y = "umschauen"
result = linear_longest_common_substring(x, y)
print(result)  # Должен вернуть (4, 9, 2, 7)

'''


