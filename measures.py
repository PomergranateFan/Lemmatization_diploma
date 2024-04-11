import numpy as np
import pickle
import pandas as pd
from config import config
from corpus_processor import UniversalDependenciesCorpus
from lemma_wordform_processor import LemmaWordformProcessorTree
from Visualization_class import VisualizationProcessor


def build_dict_with_processor(lemma_wordform_processor_class_name, corpus_name, corpus_class_name):
    '''
    Функция создает частотный словарь для разных словарей и корпусов
    :param lemma_wordform_processor_class_name: Имя процессора построения леммы в зависимости от типа правил
    :param corpus_name: имя корпуса который используется для построения словаря
    :param corpus_class_name: имя класса корпуса который используется для извлечения пар, в случае, если их нет
    :return: -
    '''

    processor = lemma_wordform_processor_class_name()

    if not config[corpus_name]['pairs'].exists():
        corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['trees'], processor,
                                   config[corpus_name]['corpus'])
        corpus.extract_lemma_wordform_pairs_not_unique()

    if not config[corpus_name]['trees'].exists():
        corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['trees'], processor,
                                   config[corpus_name]['corpus'])
        corpus.build_rules()
        corpus.save_rules_set()

    if not config[corpus_name]['dict'].exists():
        visualization_processor = VisualizationProcessor(processor, config[corpus_name]['trees'],
                                                         config[corpus_name]['pairs'], config[corpus_name]['dict'])
        visualization_processor.build_dictionary()

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


def make_dict_of_measures_for_corpus(lemma_wordform_processor_class_name, corpus_name, corpus_class_name):
    '''
    Функция создает частотный словарь для разных словарей и корпусов
    :param lemma_wordform_processor_class_name: Имя процессора построения леммы в зависимости от типа правил
    :param corpus_name: имя корпуса который используется для построения словаря
    :param corpus_class_name: имя класса корпуса который используется для извлечения пар, в случае, если их нет
    :return: -
    '''

    build_dict_with_processor(lemma_wordform_processor_class_name, corpus_name, corpus_class_name)
    K = calculate_K(config[corpus_name]['dict'], config[corpus_name]['trees'])
    slope_50 = estimate_slope(config[corpus_name]['dict'])

    return {corpus_name : {"Для процессора": lemma_wordform_processor_class_name , "K" : K, "Slope50class": slope_50}}


print(make_dict_of_measures_for_corpus(LemmaWordformProcessorTree, 'taiga', UniversalDependenciesCorpus))
'''
# Создание словаря с результатами
corpora_dict = {}


corpora_files = {
    'SynTagRus': (config['SynTagRus']['dict'], config['SynTagRus']['trees']),
    'poetry': (config['poetry']['dict'], config['poetry']['trees']),
    'taiga': (config['taiga']['dict'], config['taiga']['trees']),
    'gsd': (config['gsd']['dict'], config['gsd']['trees']),
    'pud': (config['pud']['dict'], config['pud']['trees']),
    'OpenCorpora': (config['OpenCorpora']['dict'], config['OpenCorpora']['tree']),
    'SynTagRus_original' : (config['SynTagRus_original']['dict'], config['SynTagRus_original']['trees']),
    'RNC' : (config['RNC']['dict'], config['RNC']['trees'])
}

for corpus, files in corpora_files.items():
    K = calculate_K(files[0], files[1])
    slope_50 = estimate_slope(files[0])
    corpora_dict[corpus] = {'наклон для первых 50ти классов': slope_50, 'K': K}

print(corpora_dict)

df = pd.DataFrame(corpora_dict).transpose()

print(df)
'''
