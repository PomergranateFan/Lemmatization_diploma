# Данная програма будет строить график частотного распределения деревьев,
# на котором мы надеемся увидеть распределение Парето.

import pickle
import matplotlib.pyplot as plt
from lemma_wordform_processor import LemmaWordformProcessor
from collections import defaultdict

# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

    f_x[x_counter] += 1
#    if (x_counter in f_x):
#        f_x[x_counter] += 1
#    else:
#        f_x[x_counter] = 1


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма корректна
output_file_path = 'tree_numbers_counter_uniform_not_unique_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x, output_file)

with open('tree_numbers_counter_uniform_not_unique_potential.pkl', 'rb') as f:
    data = pickle.load(f)

# Разделение данных на x и f(x)

# Построение scatter plot
plt.scatter(data.keys(), data.values(), label='log(f(x)) vs log(x)')
plt.yscale('log')
plt.xscale('log')
# Добавление подписей и легенды
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График f(x) - количество деревьев, которые корректно строят лемму по неуникальной словоформе только x раз')

plt.legend()

# Показ графика
plt.savefig('график_как_из_статьи_2_not_unique_potential.png')  # Сохраняем график

plt.show()