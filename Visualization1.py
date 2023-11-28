# Данная программа строить график:
# Число уникальных словоформ, к которым можно применить данное дерево для получения корректной леммы.

import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_new.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_new.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Создание счетчика
tree_counter = Counter()
processor = LemmaWordformProcessor()
# Внешний цикл по всем деревьям
for tree in tree_set:
    # Внутренний цикл по всем парам
    for pair in pairs:

        lemma = processor.apply(tree, pair[1])

        if lemma == pair[0]:
            tree_counter[tree] += 1

# Сохранение файла с парами дерево - число уникальных словоформ по которым лемма корректна
output_file_path = 'tree_wordform_counts_1.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(tree_counter, output_file)

# Построение графика
trees, counts = zip(*tree_counter.items())
plt.bar(trees, counts)
plt.xlabel('Индекс дерева')
plt.ylabel('Число успешных построений леммы')
plt.title('График успешных построений леммы для каждого дерева')
plt.show()
