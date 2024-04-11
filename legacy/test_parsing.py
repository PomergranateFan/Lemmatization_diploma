# Данная програма будет строить график частотного распределения деревьев,
# на котором мы надеемся увидеть распределение Парето.
import plotly.express as px

import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor
from collections import defaultdict
#~~~~~~~~~~~~~~~~~~~~~~~~~~СОБЕРЕМ f_Xы ДЛЯ ЮНИМОРФА~~~~~~~~~~~~~~
# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик

    f_x_potential[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'uni_f_x_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_potential, output_file)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_lemmas = defaultdict(int)

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

    f_x_lemmas[x_counter] += 1


# Сохранение файла с парами дерево - число неуникальных лемм
output_file_path = 'uni_f_x_lemmas.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_lemmas, output_file)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Загрузка данных из файлов
with open('tree_set_from_unimorph_test.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_Unimorph_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_correct = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

    f_x_correct[x_counter] += 1
#    if (x_counter in f_x):
#        f_x[x_counter] += 1
#    else:
#        f_x[x_counter] = 1


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма корректна
output_file_path = 'uni_f_x_correct.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_correct, output_file)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ТЕПЕРЬ ДЛЯ ОПЕНКОРПОРЫ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Загрузка данных из файлов
with open('tree_set_OpenCorpora.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_OpenCorpora_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential_corpora = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик

    f_x_potential_corpora[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'corpora_f_x_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_potential_corpora, output_file)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open('tree_set_OpenCorpora.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_OpenCorpora_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_lemmas_corpora = defaultdict(int)

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

    f_x_lemmas_corpora[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных лемм
output_file_path = 'corpora_f_x_lemmas.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_lemmas_corpora, output_file)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Загрузка данных из файлов
with open('tree_set_OpenCorpora.pkl', 'rb') as f:
    tree_set = pickle.load(f)

with open('pairs_OpenCorpora_not_unique.pkl', 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_correct_corpora = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

    f_x_correct_corpora[x_counter] += 1
#    if (x_counter in f_x):
#        f_x[x_counter] += 1
#    else:
#        f_x[x_counter] = 1


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма корректна
output_file_path = 'corpora_f_x_correct.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_correct_corpora, output_file)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ТЕПЕРЬ ДЛЯ КОРПУСА ОПЕНКОРПОРА~~~~~~~~~~~~~~~~~~~~~~~~~~



# Загрузка данных из файлов
with open(config['OpenCorpora']['tree'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['OpenCorpora']['corpus'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential_corpora_corpus = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик

    f_x_potential_corpora_corpus[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'corpora_corpus_f_x_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_potential_corpora_corpus, output_file)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(config['OpenCorpora']['tree'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['OpenCorpora']['corpus'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_lemmas_corpora_corpus = defaultdict(int)

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

    f_x_lemmas_corpora_corpus[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных лемм
output_file_path = 'corpora_corpus_f_x_lemmas.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_lemmas_corpora_corpus, output_file)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Загрузка данных из файлов
with open(config['OpenCorpora']['tree'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['OpenCorpora']['corpus'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_correct_corpora_corpus = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

    f_x_correct_corpora_corpus[x_counter] += 1
#    if (x_counter in f_x):
#        f_x[x_counter] += 1
#    else:
#        f_x[x_counter] = 1


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма корректна
output_file_path = 'corpora_corpus_f_x_correct.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_correct_corpora_corpus, output_file)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ТЕПЕРЬ ТОЖЕ САМОЕ ДЛЯ СИН ТАГ РУСА КОРПУСА~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Загрузка данных из файлов
with open(config['SynTagRus']['trees'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['SynTagRus']['pairs'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как элемент класса
processor = LemmaWordformProcessor()

f_x_potential_str = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на потенциальность
        if lemma is not None:
            x_counter += 1  # Увеличиваем счетчик

    f_x_potential_str[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма потенциальна
output_file_path = 'str_f_x_potential.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_potential_str, output_file)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open(config['SynTagRus']['trees'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['SynTagRus']['pairs'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_lemmas_str = defaultdict(int)

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

    f_x_lemmas_str[x_counter] += 1

# Сохранение файла с парами дерево - число неуникальных лемм
output_file_path = 'str_f_x_lemmas.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_lemmas_str, output_file)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Загрузка данных из файлов
with open(config['SynTagRus']['trees'], 'rb') as f:
    tree_set = pickle.load(f)

with open(config['SynTagRus']['pairs'], 'rb') as f:
    pairs = pickle.load(f)

# Заводим процессор как экземпляр класса
processor = LemmaWordformProcessor()

f_x_correct_str = defaultdict(int)

# Внешний цикл по всем деревьям
for tree in tree_set:
    x_counter = 0
    # Внутренний цикл по всем парам
    for pair in pairs:
        lemma = processor.apply(tree, pair[1])

        # Проверка на корректность
        if lemma == pair[0]:
            x_counter += 1  # Увеличиваем счетчик

    f_x_correct_str[x_counter] += 1
#    if (x_counter in f_x):
#        f_x[x_counter] += 1
#    else:
#        f_x[x_counter] = 1


# Сохранение файла с парами дерево - число неуникальных словоформ по которым лемма корректна
output_file_path = 'str_f_x_correct.pkl'
with open(output_file_path, 'wb') as output_file:
    pickle.dump(f_x_correct_str, output_file)



'''
with open('tree_numbers_counter_uniform_not_unique.pkl', 'rb') as f:
    data = pickle.load(f)

# Разделение данных на x и f(x)
x_values = list(data.keys())
y_values = list(data.values())

# Построение scatter plot
fig = px.scatter(x=x_values, y=y_values, labels={'x': 'x', 'y': 'f(x)'},
                 title='График f(x) - количество деревьев, которые потенциально строят лемму по неуникальной словоформе только x раз в лог. шкале')
fig.update_layout(xaxis_type='log', yaxis_type='log')

# Сохранение графика
# fig.write_image('TEST_график_как_из_статьи_2_not_unique.png')

# Отображение графика
fig.show()
'''
