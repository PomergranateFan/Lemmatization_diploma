# Данная программа строить Логарифмический график:
# Число уникальных словоформ, к которым можно применить данное дерево для получения корректной леммы.

import pickle
import matplotlib.pyplot as plt

# Загрузка данных из файла
# ЗАМЕЧАНИЕ: хорошо бы посмотреть на этот график для пар не уникальных, а всех.
with open('tree_wordform_counts_1_uniform.pkl', 'rb') as f:
    tree_counter = pickle.load(f)

# Построение логарифмического графика
trees, counts = zip(*tree_counter.items())
trees = [str(tree) for tree in trees]  # Преобразование в список строк

plt.bar(trees, counts)
plt.xlabel('Индекс дерева')
plt.ylabel('Число словоформ, по которым лемма строится корректно')
plt.title('Логарифмический график числа словоформ для корректных построений леммы каждым деревом')

# Скрытие оси X
plt.gca().axes.get_xaxis().set_visible(False)

# Применение логарифмической шкалы к оси Y
plt.yscale('log')

plt.savefig('tree_wordform_counts_1_uniform_log.png')  # Сохраняем график
plt.show()
