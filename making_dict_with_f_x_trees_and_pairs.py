
import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor
from collections import defaultdict
import itertools

def ddict2dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)


# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

'''
# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential = defaultdict(int)
X_dict = {}
k = 0
# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    list_tp = []

    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        k+=1
        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик
            list_tp.append((tree, pair))
    tuple_tp = tuple(list_tp)

    # f_x_potential[x_counter] += 1

    if (x_counter in X_dict):
        if k % 500 == 0:
            X_dict[x_counter] += tuple_tp
    else:
        X_dict[x_counter] = tuple_tp


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
# output_file_path = 'uni_f_x_potential_test.pkl'
# with open(output_file_path, 'wb') as output_file:
#    pickle.dump(f_x_potential, output_file)

output_file_path = "uni_f_x_potential_tree_pairs.pkl"
with open(output_file_path, 'wb') as output_file:
    pickle.dump(X_dict, output_file)
'''

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

# Словарь для хранения данных
result_dict = defaultdict(lambda: {'f_x': 0, 'trees': [], 'pairs': []})

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    pairs_list = []

    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик

            if len(pairs_list) < 5:
                pairs_list.append(pair)

    # Обновляем значения в общем словаре
    result_dict[x_counter]['f_x'] += 1
    result_dict[x_counter]['trees'].append(tree)
    result_dict[x_counter]['pairs'].extend(pairs_list)

result_dict_not_default = ddict2dict(result_dict)

output_file_path = 'uni_f_x_potential_all.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(result_dict_not_default, output_file)
