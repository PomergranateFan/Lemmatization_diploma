# данная программа строит интерактивный график, в котором
# для каждой точки показываются примеры слов и деревьев

import pickle
import plotly.express as px
import random
from LemmaWordformProcessor_class import LemmaWordformProcessor

with open('uni_f_x_potential_all.pkl', 'rb') as f:
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
