'''
Данная программа строит график:
Число уникальных лемм,которые можно получить в результате применения данного дерева к различным слоформам
'''
import pickle
from collections import Counter
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_from_unimorph_test.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

# Создание счетчика уникальных лемм по деревьям
unique_lemma_counter = Counter()

# Внешний цикл по всем деревьям
for tree in tree_set:
    # Список для отслеживания уникальных лемм для текущего дерева
    unique_lemmas_for_tree = set()

    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])
        if lemma is not None:
            unique_lemmas_for_tree.add(lemma)

    # Записываем количество уникальных лемм для текущего дерева
    unique_lemma_counter[tree] = len(unique_lemmas_for_tree)

# Сохранение файла с парами дерево - количество уникальных лемм
output_file_path = 'unique_lemma_tree_counts_uniform.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(unique_lemma_counter, output_file)

# Построение графика

# Построение графика
trees, counts = zip(*unique_lemma_counter.items())
trees = [str(tree) for tree in trees]  # Преобразование в список строк
plt.bar(trees, counts)
plt.xlabel('Деревья')
plt.ylabel('Число потенциально полученных лемм(log)')
plt.title('Логарифмичесий график числа уникальных лемм, которые могут быть потенцаильно получены каждым деревом')
# Скрытие оси X
plt.gca().axes.get_xaxis().set_visible(False)
plt.yscale('log')

plt.savefig('unique_lemma_tree_counts_uniform_log.png')  # Сохраняем график
plt.show()
