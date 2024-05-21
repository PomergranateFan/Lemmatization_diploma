
from lemma_wordform_processor import LemmaWordformProcessorTree
from lemma_wordform_processor import LemmaWordformProcessorSES
from lemma_wordform_processor import LemmaWordformProcessorUDWithCopy
from lemma_wordform_processor import LemmaWordformProcessorUDWithoutCopy
from visualization_class import VisualizationProcessor
from corpus_processor import UniversalDependenciesCorpus
from corpus_processor import OpenCorporaCorpus
from corpus_processor import BaseDictionaryCorpus
from config import config
import pickle


processor_corpuses_and_classes = [(LemmaWordformProcessorTree, 'SynTagRus', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorSES, 'SynTagRus', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'SynTagRus', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'SynTagRus', UniversalDependenciesCorpus),

                        (LemmaWordformProcessorTree, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorSES, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'poetry', UniversalDependenciesCorpus),

                        (LemmaWordformProcessorTree, 'taiga', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorSES, 'taiga', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'taiga', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'taiga', UniversalDependenciesCorpus),

                        (LemmaWordformProcessorTree, 'gsd', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorSES, 'gsd', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'gsd', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'gsd', UniversalDependenciesCorpus),

                        (LemmaWordformProcessorTree, 'pud', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorSES, 'pud', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'pud', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'pud', UniversalDependenciesCorpus),

                        (LemmaWordformProcessorTree, 'OpenCorpora', OpenCorporaCorpus),
                        (LemmaWordformProcessorSES, 'OpenCorpora', OpenCorporaCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'OpenCorpora', OpenCorporaCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'OpenCorpora', OpenCorporaCorpus),

                        (LemmaWordformProcessorTree, 'SynTagRus_original', BaseDictionaryCorpus),
                        (LemmaWordformProcessorSES, 'SynTagRus_original', BaseDictionaryCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'SynTagRus_original', BaseDictionaryCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'SynTagRus_original', BaseDictionaryCorpus),

                        (LemmaWordformProcessorTree, 'RNC', BaseDictionaryCorpus),
                        (LemmaWordformProcessorSES, 'RNC', BaseDictionaryCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'RNC', BaseDictionaryCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'RNC', BaseDictionaryCorpus)
                        ]



processor_corpuses_and_classes_test = [
                        (LemmaWordformProcessorTree, 'poetry', UniversalDependenciesCorpus),
                        #(LemmaWordformProcessorSES, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'poetry', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorTree, 'gsd', UniversalDependenciesCorpus),
                        #(LemmaWordformProcessorSES, 'gsd', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithoutCopy, 'gsd', UniversalDependenciesCorpus),
                        (LemmaWordformProcessorUDWithCopy, 'gsd', UniversalDependenciesCorpus),
                            ]

def build_dict_with_processor(lemma_wordform_processor_class_name, corpus_name, corpus_class_name):

    
    '''
    Функция создает частотный словарь для разных словарей и корпусов
    :param lemma_wordform_processor_class_name: Имя процессора построения леммы в зависимости от типа правил
    :param corpus_name: имя корпуса который используется для построения словаря
    :param corpus_class_name: имя класса корпуса который используется для извлечения пар, в случае, если их нет
    :return: -
    '''
    


    processor = lemma_wordform_processor_class_name

    if not config[corpus_name]['pairs'].exists():
        corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['trees'], processor,
                                   config[corpus_name]['corpus'])
        corpus.extract_lemma_wordform_pairs_not_unique()

    if lemma_wordform_processor_class_name == LemmaWordformProcessorTree:
        if not config[corpus_name]['trees'].exists():
            corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['trees'], processor,
                                       config[corpus_name]['corpus'])
            corpus.build_rules()
            corpus.save_rules_set()

        if not config[corpus_name]['dict_tree'].exists():
            visualization_processor = VisualizationProcessor(processor, config[corpus_name]['trees'],
                                                             config[corpus_name]['pairs'],
                                                             config[corpus_name]['dict_tree'])
            visualization_processor.build_dictionary()

    if lemma_wordform_processor_class_name == LemmaWordformProcessorSES:
        if not config[corpus_name]['ses'].exists():
            corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['ses'], processor,
                                       config[corpus_name]['corpus'])
            corpus.build_rules()
            corpus.save_rules_set()

        if not config[corpus_name]['dict_ses'].exists():
            visualization_processor = VisualizationProcessor(processor, config[corpus_name]['ses'],
                                                             config[corpus_name]['pairs'],
                                                             config[corpus_name]['dict_ses'])
            visualization_processor.build_dictionary()

    if lemma_wordform_processor_class_name == LemmaWordformProcessorUDWithCopy:
        if not config[corpus_name]['ud_with_copy'].exists():
            corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['ud_with_copy'], processor,
                                       config[corpus_name]['corpus'])
            corpus.build_rules()
            corpus.save_rules_set()

        if not config[corpus_name]['dict_ud_with_copy'].exists():
            visualization_processor = VisualizationProcessor(processor, config[corpus_name]['ud_with_copy'],
                                                             config[corpus_name]['pairs'],
                                                             config[corpus_name]['dict_ud_with_copy'])
            visualization_processor.build_dictionary()

    if lemma_wordform_processor_class_name == LemmaWordformProcessorUDWithoutCopy:
        if not config[corpus_name]['ud_without_copy'].exists():
            corpus = corpus_class_name(config[corpus_name]['pairs'], config[corpus_name]['ud_without_copy'], processor,
                                       config[corpus_name]['corpus'])
            corpus.build_rules()
            corpus.save_rules_set()

        if not config[corpus_name]['dict_ud_without_copy'].exists():
            visualization_processor = VisualizationProcessor(processor, config[corpus_name]['ud_without_copy'],
                                                             config[corpus_name]['pairs'],
                                                             config[corpus_name]['dict_ud_without_copy'])
            visualization_processor.build_dictionary()

'''
# Это не работает
for item in processor_corpuses_and_classes_test:
    build_dict_with_processor(item[0], item[1], item[2])
'''

'''
processor_names = [LemmaWordformProcessorSES, LemmaWordformProcessorTree, LemmaWordformProcessorUDWithoutCopy, LemmaWordformProcessorUDWithCopy]
a = "."
b = "."
for processor_name in processor_names:
    processor = processor_name()
    rule = processor.build_rule(a,b)

    print(rule)
'''


def create_rule_dict(rule_set_file_path, output_file_path):
    # Загрузка множества правил из файла rule_set.pkl
    with open(rule_set_file_path, 'rb') as f:
        rule_set = pickle.load(f)

        # Преобразование множества в кортеж
    rule_tuple = tuple(rule_set)

    # Создание словаря с правилами и их метками
    rule_dict = {}
    for rule in rule_tuple:
        rule_dict[rule] = rule_tuple.index(rule) + 1  # Индекс в кортеже + 1 для получения метки

    # Сохранение словаря в файл output_file_path
    with open(output_file_path, 'wb') as f:
        pickle.dump(rule_dict, f)

'''
rules = ["trees", "ses", "ud_with_copy", "ud_without_copy"]
corpus_names = ['SynTagRus_original', 'OpenCorpora', 'pud', 'RNC']


for corpus_name in corpus_names:
    for rule in rules:
        rule_set_file_path = config[corpus_name][rule]
        ouput_name = "labels_"+rule
        output_file_path = config[corpus_name][ouput_name]
        create_rule_dict(rule_set_file_path, output_file_path)
        
'''

# Посторим частотные графики для словарей gsd и poetry:
processor_names_rules = {LemmaWordformProcessorTree : 'trees', LemmaWordformProcessorUDWithCopy : "ud_with_copy", LemmaWordformProcessorUDWithoutCopy : "ud_without_copy"}
corpus_names = [ 'taiga', 'SynTagRus']

for processor_name in processor_names_rules.items():
    for corpus_name in corpus_names:

        dict_name = 'dict_' + processor_name[1]
        visualization_processor = VisualizationProcessor(processor_name[0], config[corpus_name][processor_name[1]],
                                                  config[corpus_name]['pairs'], config[corpus_name][dict_name])

        visualization_processor.build_dictionary()
        visualization_processor.visualize()

'''
processor = LemmaWordformProcessorSES()
wordform= 'прибежал'
lemma = 'бежит'
rule = processor.build_rule(wordform, lemma)
print(rule)
lemma_test = processor.apply_rule(rule, wordform)
print(lemma_test)
'''





