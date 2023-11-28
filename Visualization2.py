# Данная программа строит график:
# Число уникальных словоформ, к которым можно потенциально применить данное дерево(результатом работы не будет None).

import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_new_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_new.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

# Создание счетчика словоформ по деревьям, которые потенциально можно применить к ним.
potential_tree_counter = Counter()

# Внешний цикл по всем деревьям
for tree in tree_set:
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])
        if lemma is not None:  # Результат применения дерева к словоформе какой-то но получается
            potential_tree_counter[tree] += 1

# Сохранение файла с парами дерево - число уникальных словоформ по которым лемма корректна
output_file_path = 'potential_tree_wordform_counts_2.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(potential_tree_counter, output_file)


# Построение графика
trees, counts = zip(potential_tree_counter.items())
plt.bar(trees, counts)
plt.xlabel('Деревья')
plt.ylabel('Число потенциальных построений леммы')
plt.title('График потенциальных построений леммы для каждого дерева')
plt.show()
