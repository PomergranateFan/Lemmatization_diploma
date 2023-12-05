'''
График отображает количество деревьев, которые могут быть применены к каждой словоформе для получения уникальной леммы.
'''
import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_new_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_new.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заведем процессор как элемент класса
processor = LemmaWordformProcessor()

# Создание счетчика уникальных деревьев для каждой словоформы
unique_tree_counter = Counter()

# Внешний цикл по всем словоформам
for pair in pairs:
    # Множество для отслеживания уникальных деревьев для текущей словоформы
    unique_trees_for_wordform = set()

    # Внутренний цикл по всем деревьям
    for tree in tree_set:
        lemma = processor.apply(tree, pair[1])
        if lemma is not None:
            unique_trees_for_wordform.add(tree)

    # Записываем количество уникальных деревьев для текущей словоформы
    unique_tree_counter[pair[1]] = len(unique_trees_for_wordform)

# Сохранение файла с парами словоформа - количество уникальных деревьев
output_file_path = 'unique_tree_wordform_counts.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(unique_tree_counter, output_file)

# Построение графика
wordforms, counts = zip(*unique_tree_counter.items())
plt.bar(wordforms, counts)
plt.xlabel('Cловоформа')
plt.ylabel('Число уникальных деревьев')
plt.title('количество деревьев, которые могут быть применены к каждой словоформе для получения уникальной леммы.')
plt.show()
