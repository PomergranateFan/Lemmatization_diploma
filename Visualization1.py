# Данная программа строит логарифмический график:
# Число уникальных словоформ, к которым можно применить данное дерево для получения корректной леммы.

import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_from_unimorph.pkl', 'rb') as f:
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
output_file_path = 'tree_wordform_counts_1_uniform.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(tree_counter, output_file)

# Загрузка данных из файла
# ЗАМЕЧАНИЕ: хорошо бы посмотреть на этот график для пар не уникальных, а всех.
with open('tree_wordform_counts_1_uniform.pkl', 'rb') as f:
    tree_counter = pickle.load(f)

# Построение логарифмического графика
trees, counts = zip(*tree_counter.items())
trees = [str(tree) for tree in trees]  # Преобразование в список строк

plt.bar(trees, counts)
plt.xlabel('Деревья')
plt.ylabel('Число словоформ, по которым лемма строится корректно')
plt.title('Логарифмический график числа словоформ для корректных построений леммы каждым деревом')

# Скрытие оси X
plt.gca().axes.get_xaxis().set_visible(False)

# Применение логарифмической шкалы к оси Y
plt.yscale('log')

plt.savefig('tree_wordform_counts_1_uniform_log.png')  # Сохраняем график
plt.show()