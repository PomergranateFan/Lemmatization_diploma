# Данная программа строит логарифмический график:
# Число уникальных лемм,которые можно получить в результате применения данного дерева к различным слоформам
import pickle
import matplotlib.pyplot as plt

with open('unique_lemma_tree_counts_uniform.pkl', 'rb') as f:
    unique_lemma_counter = pickle.load(f)



# Построение графика
trees, counts = zip(*unique_lemma_counter.items())
trees = [str(tree) for tree in trees]  # Преобразование в список строк
plt.bar(trees, counts)
plt.xlabel('Деревья')
plt.ylabel('Число потенциально полученных лемм(log)')
plt.title('Логарифмичесий рафик числа уникальных лемм, которые могут быть потенцаильно получены каждым деревом')
# Скрытие оси X
plt.gca().axes.get_xaxis().set_visible(False)
plt.yscale('log')

plt.savefig('unique_lemma_tree_counts_uniform_log.png')  # Сохраняем график
plt.show()
