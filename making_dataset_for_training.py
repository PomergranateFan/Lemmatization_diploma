import pickle
from conllu import parse
from lemma_wordform_processor import LemmaWordformProcessorTree
from config import config

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
def load_trees(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


processor = LemmaWordformProcessorTree()

# Функция для получения метки класса по словоформе и лемме
def get_label(wordform, lemma, trees_tuple):
    tree = processor.build_rule(wordform, lemma)

    if tree in trees_tuple:
        index = trees_tuple.index(tree)
        return index
    else:
        return None


# Функция для обработки файла и записи результата в новый файл
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

