import pickle
from collections import Counter
import matplotlib.pyplot as plt
from Tree_function import TREE_tuple
from APPLY_function import APPLY

# Открываем файл для чтения
with open('lemma_wordform_pair.pkl', 'rb') as file:
    data = pickle.load(file)
dic = Counter()
# Выводим часть данных для проверки
for i, pair in enumerate(data[:2000]):  # Вывести первые n пар
    # print((pair))
    tree = TREE_tuple(pair[1], pair[0])
    lemma = APPLY(tree, pair[1])

    dic[lemma] += 1

# Закрываем файл
file.close()
print(dic)



# Разделение ключей и значений
lemmas = list(dic.keys())
lemmas_counts = list(dic.values())

# Создание гистограммы
plt.figure(figsize=(100, 15))
plt.bar(lemmas, lemmas_counts)
plt.xlabel('лемма')
plt.ylabel('Количество слов')
plt.title('Распределение слов')
plt.xticks(rotation=45)  # Поворот меток по оси X для лучшей видимости

# Отображение графика
plt.tight_layout()
plt.show()

