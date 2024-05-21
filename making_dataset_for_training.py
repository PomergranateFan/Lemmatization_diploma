import pickle
from conllu import parse
from lemma_wordform_processor import LemmaWordformProcessorTree
from lemma_wordform_processor import LemmaWordformProcessorSES
from lemma_wordform_processor import LemmaWordformProcessorUDWithoutCopy
from lemma_wordform_processor import LemmaWordformProcessorUDWithCopy
from config import config
from pathlib import Path


# Функция для преобразования множества в кортеж
def set_to_tuple(data_set):
    return tuple(data_set)


# Функция для извлечения словоформ и меток из предложения
def extract_tokens(sentence):
    tokens = []
    for token in sentence:
        wordform = token['form']
        lemma = token['lemma']
        tokens.append((wordform.lower(), lemma.lower()))
    return tokens


# Загрузка словаря деревьев из файла
def load_file(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)




# Функция для получения метки класса по словоформе и лемме
def get_label(processor_name, wordform, lemma, labels_trees, base_rule):
    processor = processor_name()
    rule = processor.build_rule(wordform, lemma)
    if rule in labels_trees:
        index = labels_trees[rule]
    else:
        index = labels_trees[base_rule]# Так мы убираем ошибки из датасетов, связанные с пунктуацией
    return index

# Функция для обработки файла и записи результата в новый файл
def process_file(processor_name, input_file, output_file, labels_trees, base_rule):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        data = f_in.read()
        sentences = parse(data)
        for sentence in sentences:
            tokens = extract_tokens(sentence)
            for wordform, lemma in tokens:
                class_label = get_label(processor_name, wordform, lemma, labels_trees, base_rule)
                f_out.write(f"{wordform}\t{class_label}\n")
            f_out.write('\n')
'''
corpus_file = 'data/poetry/corpus/ru_poetry-ud-test.conllu'
trees_file = 'data/poetry/tree_set_poetry_corpus.pkl'

corpus_file_1 = 'data/poetry/corpus/ru_poetry-ud-dev.conllu'

# Загрузка множества деревьев из файла
trees_set = load_trees(trees_file)
# Преобразование множества в кортеж
trees_tuple = set_to_tuple(trees_set)
# Обработка корпуса и запись результата в файл
process_file(corpus_file, 'dataset_poetry_test.txt', trees_tuple)
process_file(corpus_file_1, 'dataset_poetry_dev.txt', trees_tuple)
'''

corpus_names = ['SynTagRus', 'taiga']
rules = ['trees', 'ses', 'ud_with_copy', 'ud_without_copy']

for corpus_name in corpus_names:
    for rule in rules:
        corpus_file = config[corpus_name]['corpus']
        name_labels = "labels_" + rule
        rules_dict = load_file(config[corpus_name][name_labels])

        for file_path in corpus_file.iterdir():
            print(file_path)
            if file_path.suffix == '.conllu':
                if file_path.stem.endswith('test'):

                    if rule == 'trees':
                        if not config[corpus_name]['dataset_tree_test'].exists():
                            processor_name = LemmaWordformProcessorTree
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_tree_test'], rules_dict, base_rule)
                    elif rule == 'ses':
                        if not config[corpus_name]['dataset_ses_test'].exists():
                            processor_name = LemmaWordformProcessorSES
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ses_test'], rules_dict, base_rule)
                    elif rule == 'ud_with_copy':
                        if not config[corpus_name]['dataset_ud_with_copy_test'].exists():
                            processor_name = LemmaWordformProcessorUDWithCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_with_copy_test'], rules_dict, base_rule)
                    elif rule == 'ud_without_copy':
                        if not config[corpus_name]['dataset_ud_without_copy_test'].exists():
                            processor_name = LemmaWordformProcessorUDWithoutCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_without_copy_test'], rules_dict, base_rule)

                elif file_path.stem.endswith('train'):

                    if rule == 'trees':
                        if not config[corpus_name]['dataset_tree_train'].exists():
                            processor_name = LemmaWordformProcessorTree
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_tree_train'], rules_dict, base_rule)
                    elif rule == 'ses':
                        if not config[corpus_name]['dataset_ses_train'].exists():
                            processor_name = LemmaWordformProcessorSES
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ses_train'], rules_dict, base_rule)
                    elif rule == 'ud_with_copy':
                        if not config[corpus_name]['dataset_ud_with_copy_train'].exists():
                            processor_name = LemmaWordformProcessorUDWithCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_with_copy_train'], rules_dict, base_rule)
                    elif rule == 'ud_without_copy':
                        if not config[corpus_name]['dataset_ud_without_copy_train'].exists():
                            processor_name = LemmaWordformProcessorUDWithoutCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_without_copy_train'], rules_dict, base_rule)

                elif file_path.stem.endswith('dev'):

                    if rule == 'trees':
                        if not config[corpus_name]['dataset_tree_dev'].exists():
                            processor_name = LemmaWordformProcessorTree
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_tree_dev'], rules_dict, base_rule)
                    elif rule == 'ses':
                        if not config[corpus_name]['dataset_ses_dev'].exists():
                            processor_name = LemmaWordformProcessorSES
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ses_dev'], rules_dict, base_rule)
                    elif rule == 'ud_with_copy':
                        if not config[corpus_name]['dataset_ud_with_copy_dev'].exists():
                            processor_name = LemmaWordformProcessorUDWithCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_with_copy_dev'], rules_dict, base_rule)
                    elif rule == 'ud_without_copy':
                        if not config[corpus_name]['dataset_ud_without_copy_dev'].exists():
                            processor_name = LemmaWordformProcessorUDWithoutCopy
                            base_rule = processor_name().build_rule(".", ".")
                            process_file(processor_name, file_path, config[corpus_name]['dataset_ud_without_copy_dev'], rules_dict, base_rule)




'''
class BaseMakingDataset:
    def __init__(self, lemma_wordform_processor_class_name, corpus_name, corpus_class_name):
        """
        Инициализация базового класса для построения датасетов для разных корпусов и разных правил

        Args:
            :param lemma_wordform_processor_class_name: Имя процессора построения леммы в зависимости от типа правил
            :param corpus_name: имя корпуса который используется для построения датасета
            :param corpus_class_name: имя класса корпуса который используется для парсинга слов

        """
        self.processor = lemma_wordform_processor_class_name()
        self.corpus_name = corpus_class_name
        self.corpus_class_name = corpus_class_name
    @staticmethod
    def set_to_tuple(data_set):
        return tuple(data_set)

    @staticmethod
    def load_trees(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def get_label(wordform, lemma, trees_tuple):
        tree = processor.build_rule(wordform, lemma)

        if tree in trees_tuple:
            index = trees_tuple.index(tree)
            return index + 1  # возвращаем индекс+1 как метку, чтобы 0 был для дополнения.

class MakingDatasetUD(BaseMakingDataset):
    def __init__(self, lemma_wordform_processor_class_name, corpus_name, corpus_class_name):
        """
        Инициализация базового класса для построения датасетов для разных корпусов и разных правил

        Args:
            :param lemma_wordform_processor_class_name: Имя процессора построения леммы в зависимости от типа правил
            :param corpus_name: имя корпуса который используется для построения датасета
            :param corpus_class_name: имя класса корпуса который используется для парсинга слов

        """
        super().__init__(self, lemma_wordform_processor_class_name, corpus_name, corpus_class_name)

    def process_file(input_file, output_file, trees_tuple):
        with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
            data = f_in.read()
            sentences = parse(data)
            for sentence in sentences:
                tokens = extract_tokens(sentence)
                for wordform, lemma in tokens:
                    class_label = get_label(wordform, lemma, trees_tuple)
                    f_out.write(f"{wordform}\t{class_label}\n")
                f_out.write('\n')

    def extract_tokens(sentence):
        tokens = []
        for token in sentence:
            wordform = token['form']
            lemma = token['lemma']
            tokens.append((wordform.lower(), lemma.lower()))
        return tokens
'''

