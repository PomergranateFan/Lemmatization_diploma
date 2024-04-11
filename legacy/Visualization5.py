'''
Данная программа строить график:
Число деревьев, которые можно потенциально применить к словоформам(результатом работы не будет None).
'''
import pickle
from collections import Counter
import matplotlib.pyplot as plt
from lemma_wordform_processor import LemmaWordformProcessor

# Загрузка данных из файлов
with open('tree_set_new_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('lemma_wordform_pair_new_test.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заведем пустой элемент класса
processor = LemmaWordformProcessor()
# Создание счетчика
potential_wordform_tree_counter = Counter()

# Внешний цикл по всем словоформам
for pair in pairs:
    # Внутренний цикл по всем деревьям
    for tree in tree_set:

        lemma = processor.apply(tree, pair[1])

        if lemma is not None:  # Результат применения дерева к словоформе какой-то, и он не является None
            potential_wordform_tree_counter[pair[1]] += 1

# Сохранение файла с парами словоформа - количество деревьев, по которым потенциально строятся корректные леммы
output_file_path = 'potential_lemma_tree_counts.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(potential_wordform_tree_counter, output_file)

# Построение графика
wordforms, counts = zip(*potential_wordform_tree_counter.items())
plt.bar(wordforms, counts)
plt.xlabel('Cловоформа')
plt.ylabel('Число деревьев, потенциально успешно построивших лемму')
plt.title('График числа деревьев, потенциально построивших лемму для каждой словоформы')
plt.show()
