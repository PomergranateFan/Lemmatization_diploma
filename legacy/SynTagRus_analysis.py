# В данной программе строится интерактивный частотный график корректных построений пар для копруса
# пар для копруса SynTagRus для анализа хвоста графика

import plotly.express as px
import random
import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor
from collections import defaultdict

def ddict2dict(d):
    '''
    функция возращает обычный словарь по default дикту
    :param d: default dict
    :return: dict
    '''
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)


# Загрузка данных из файлов
with open('tree_set_SynTagRus_corpus.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_SynTagRus_corpus_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

# Словарь для хранения данных
result_dict = defaultdict(lambda: {'f_x': 0, 'trees': [], 'pairs': []})

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    pairs_list = []

    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

            if len(pairs_list) < 5:
                pairs_list.append(pair)

    # Обновляем значения в общем словаре
    result_dict[x_counter]['f_x'] += 1
    result_dict[x_counter]['trees'].append(tree)
    result_dict[x_counter]['pairs'].extend(pairs_list)

result_dict_not_default = ddict2dict(result_dict)

output_file_path = 'str_f_x_correct_all.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(result_dict_not_default, output_file)

with open('str_f_x_correct_all.pkl', 'rb') as f:
    result_dict = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

# Создаем списки для оси x и y, а также для текста (информации о деревьях и парах)
x_values = []
y_values = []
text_info = []

# Заполняем списки данными из result_dict
for x_counter, values in result_dict.items():
    x_values.append(x_counter)
    y_values.append(values['f_x'])

    # Выбираем случайные 3 дерева и пары из всей выборки
    #random_trees = random.sample(values['trees'], min(2, len(values['trees'])))
    values['pairs'] = [pair for pair in values['pairs'] if ' ' not in pair[0]]
    random_pairs = random.sample(values['pairs'], min(3, len(values['pairs'])))
    pairs = []
    for lemma, wordform in random_pairs:
        tree = processor.build_tree(lemma, wordform)
        pairs.append((tree, lemma, wordform))
    random_pairs = pairs

    #tree_info = '\n'.join([f"{tree}" for tree in random_trees])
    pair_info = '\n'.join([f"{pair}" for pair in random_pairs])
    text_info.append(
        f"\nPairs:\n{pair_info}")
        #f"\nTrees:\n{tree_info}\nPairs:\n{pair_info}")

# Создаем scatter plot с использованием Plotly
fig = px.scatter(x=x_values, y=y_values, hover_data={'text': text_info}, labels={'x': 'x_counter', 'y': 'f_x'},
                 title='Частотный график')

fig.update_xaxes(type='log')
fig.update_yaxes(type='log')

# Отображаем график
fig.show()

