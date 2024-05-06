
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


for item in processor_corpuses_and_classes:
    build_dict_with_processor(item[0], item[1], item[2])


