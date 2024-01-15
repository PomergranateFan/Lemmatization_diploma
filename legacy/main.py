
import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor
from collections import defaultdict

# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)[:50]

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)[:100]

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = [0, tree, None]
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter[0] += 1  # Увеличиваем счетчик
            x_counter[2] = pair

        f_x_potential[x_counter[0]].append([x_counter[1], x_counter[2]])

# Выводим результат
for count, values in f_x_potential.items():
    print(f"Count {count}: {values}")

'''
# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'uni_f_x_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_potential, output_file)
'''
