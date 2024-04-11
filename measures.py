import numpy as np
import pickle
import pandas as pd


def calculate_K(file1, file2):
    '''
    Считает коэффициент k
    :param file1: файл, содержащий частотную информацию о правилах
    :param file2: файл с множеством правил
    :return: Yule's K - инвариантный отностительно размера коэффициент
    '''

    with open(file1, 'rb') as f:
        f_x_data = pickle.load(f)

    with open(file2, 'rb') as f:
        tree_set = pickle.load(f)

    sum_x = 0
    N = len(tree_set)

    for x, info in f_x_data.items():
        f_x = info['f_x']
        sum_x += f_x * ((x / N) ** 2)

    K = (-1 / N + sum_x)
    return K



def estimate_slope(file_path):
    """
    Оценивает наклон прямой методом наименьших квадратов для первых 50 классов
    :param file_path : str Путь к файлу .pkl, содержащему словарь данных.
    :return slope : float Оценка наклона прямой методом наименьших квадратов.
    """
    # Загрузка данных из файла .pkl
    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    # Извлечение данных до 50
    x_values = np.array([x for x in data.keys() if x <= 50])
    f_values = np.array([data[x]['f_x'] for x in x_values])

    # Оценка наклона прямой (МНК)
    slope, _ = np.polyfit(x_values, f_values, 1)

    return slope

# Создание словаря с результатами
corpora_dict = {}


corpora_files = {
    'SynTagRus': ('syntagrus_f_x_dict.pkl', 'tree_set_SynTagRus_corpus.pkl'),
    'poetry': ('poetry_f_x_dict.pkl', 'tree_set_poetry_corpus.pkl'),
    'taiga': ('taiga_f_x_dict.pkl', 'tree_set_taiga_corpus.pkl'),
    'gsd': ('gsd_f_x_dict.pkl', 'tree_set_gsd_corpus.pkl'),
    'pud': ('pud_f_x_dict.pkl', 'tree_set_pud_corpus.pkl'),
    'OpenCorpora': ('OpenCorpora_f_x_dict.pkl', 'tree_set_OpenCorpora_corpus.pkl'),
    'SynTagRus_original' : ("syntagrus_original_f_x_dict.pkl", 'tree_set_SynTagRus_original_corpus.pkl'),
    'RNC' : ('RNC_main_f_x_dict.pkl', 'tree_set_RNC_main_corpus.pkl')
}

for corpus, files in corpora_files.items():
    K = calculate_K(files[0], files[1])
    slope_50 = estimate_slope(files[0])
    corpora_dict[corpus] = {'наклон для первых 50ти классов': slope_50, 'K': K}

print(corpora_dict)

df = pd.DataFrame(corpora_dict).transpose()

print(df)