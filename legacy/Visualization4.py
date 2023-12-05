# Данная программа строить график:
# Число деревьев, которые можно применить к словоформе для получения корректной леммы.

import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_new_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_new_test.pkl', 'rb') as f:
    pairs = pickle.load(f)


# Заведем пустой элемент класса
processor = LemmaWordformProcessor()
# Создание счетчика
wordform_tree_counter = Counter()

# Внешний цикл по всем словоформам
for pair in pairs:
    # Внутренний цикл по всем деревьям
    for tree in tree_set:

        lemma = processor.apply(tree, pair[1])

        if lemma == pair[0]:
            wordform_tree_counter[pair[1]] += 1

# Сохранение файла с парами словоформа - количество деревьев, по которым строятся корректные леммы
output_file_path = 'unique_lemma_tree_counts.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(wordform_tree_counter, output_file)


# Построение графика
wordforms, counts = zip(*wordform_tree_counter.items())
plt.bar(wordforms, counts)
plt.xlabel('Cловоформа')
plt.ylabel('Число дереревьев, успешно построивших корректную лемму')
plt.title('График числа дереьвев, успешно построивших корректную лемму для каждой словоформы')
plt.show()
