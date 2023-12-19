# Данная програма будет строить график частотного распределения деревьев,
# на котором мы надеемся увидеть распределение Парето.
# для f(x) - кол-во деревьев, которые при применении дают определенную лемму только x раз

import pickle
import matplotlib.pyplot as plt
from LemmaWordformProcessor_class import LemmaWordformProcessor
from collections import defaultdict

# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

print(f" Количевство деревьев {len(tree_set)}")

print(f" Количевство пар {len(pairs)}")
# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    unique_lemmas_for_tree = set()
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на новизну
        if lemma not in unique_lemmas_for_tree:
            x_counter += 1  # Увеличиваем счетчик
            unique_lemmas_for_tree.add(lemma)

    f_x[x_counter] += 1

print(f"сумма иксов {sum(f_x.keys())}, сумма f(x) {sum(f_x.values())} должно быть равно количеству деревьев")


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'tree_numbers_counter_uniform_not_unique_for_lemmas.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x, output_file)

with open('tree_numbers_counter_uniform_not_unique_for_lemmas.pkl', 'rb') as f:
    data = pickle.load(f)

# Разделение данных на x и f(x)

# Построение scatter plot
plt.scatter(data.keys(), data.values(), label='log(f(x)) vs log(x)')
plt.yscale('log')
plt.xscale('log')
# Добавление подписей и легенды
plt.xlabel('log(x)')
plt.ylabel('log(f(x))')
plt.title('График f(x) - количество деревьев, по которым можно построить конкретную лемму только x раз')

plt.legend()

# Показ графика
# plt.savefig('график_как_из_статьи_для_лемм_not_unique.png')  # Сохраняем график

plt.show()

