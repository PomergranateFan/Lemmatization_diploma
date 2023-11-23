# Данная программа строить график:
# Число уникальных словоформ, к которым можно применить данное дерево для получения корректной леммы.

import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_full.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_full.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Создание счетчика
tree_counter = Counter()

# Внешний цикл по всем деревьям
for i, tree in enumerate(tree_set):
    # Внутренний цикл по всем парам
    for pair in pairs:

        processor = LemmaWordformProcessor(pair[0], pair[1]) # класс(лемма ,слоформа)
        processor.set_tree(tree) # устанавливаем дерево из множества, чтобы не строить его в цикле
        lemma = processor.apply(pair[1])

        if lemma == pair[0]:
            tree_counter[i] += 1

# Построение графика
trees, counts = zip(*tree_counter.items())
plt.bar(trees, counts)
plt.xlabel('Индекс дерева')
plt.ylabel('Число успешных построений леммы')
plt.title('График успешных построений леммы для каждого дерева')
plt.show()
