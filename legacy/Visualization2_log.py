# Данная программа строит Логарифмический график:
# Число уникальных словоформ, к которым можно потенциально применить данное дерево(результатом работы не будет None).

import pickle
import matplotlib.pyplot as plt

with open('potential_tree_wordform_counts_2_uniform.pkl', 'rb') as f:
    potential_tree_counter = pickle.load(f)


# Построение графика
trees, counts = zip(*potential_tree_counter.items())
trees = [str(tree) for tree in trees]  # Преобразование в список строк
plt.bar(trees, counts)
plt.xlabel('Индекс дерева')
plt.ylabel('Число словоформ, по которым лемма строится потенцильно')
plt.title('Логарифмический график числа словоформ для потенциальных построений леммы каждым деревом')
# Скрытие оси X
plt.gca().axes.get_xaxis().set_visible(False)

# Применение логарифмической шкалы к оси Y
plt.yscale('log')

plt.savefig('potential_tree_wordform_counts_2_uniform_log.png')  # Сохраняем график

plt.show()
