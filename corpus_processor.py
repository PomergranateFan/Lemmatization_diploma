import pickle
import xml.etree.ElementTree as ET
from lemma_wordform_processor import LemmaWordformProcessor
from conllu import parse
import os


class BaseDictionaryCorpus:
    def __init__(self, input_file, output_file, lemma_wordform_processor_class_name, data_path = None):
        """
        Инициализация базового класса для работы с словарями и корпусами.

        Args:
            data_path (str): Путь к исходным данным (например, XML-файл словаря или корпуса).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
            lemma_wordform_processor_class_name (str): Имя класса лемма-вордформ_процессора
        """
        self.data_path = data_path
        self.input_file = input_file
        self.output_file = output_file
        self.rules_set = set()
        self.processor = lemma_wordform_processor_class_name()

    def build_rules(self):
        """
        Метод для построения деревьев на основе пар лемма-словоформа.

        Проходит через пары лемма-словоформа и строит деревья с помощью LemmaWordformProcessor.

        Returns:
            None
        """
        with open(self.input_file, 'rb') as file:
            data = pickle.load(file)

        for pair in data:
            lemma, wordform = pair
            tree = self.processor.build_rule(wordform.lower(), lemma.lower())  # Convert to lowercase
            self.rules_set.add(tree)

        file.close()

    def save_rules_set(self):
        """
        Метод для сохранения деревьев в файл.

        Сохраняет построенные деревья в файл в формате pickle.

        Returns:
            None
        """
        with open(self.output_file, 'wb') as file:
            pickle.dump(self.rules_set, file)


    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного словаря.

        Проходит через файл и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        raise NotImplementedError("Метод должен быть реализован в подклассе!")


class OpenCorpora(BaseDictionaryCorpus):
    def __init__(self, input_file, output_file, lemma_wordform_processor_class_name, data_path):
        """
        Инициализация класса OpenCorpora для работы с данными OpenCorpora.

        Args:
            data_path (str): Путь к исходным данным OpenCorpora (XML-файл словаря OpenCorpora).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(input_file, output_file, lemma_wordform_processor_class_name, data_path)

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного XML-файла OpenCorpora.

        Проходит через XML-файл OpenCorpora и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        tree = ET.parse(self.data_path)
        root = tree.getroot()
        lemma_wordform_pairs = set()

        for lemma in root.find("lemmata").iter("lemma"):
            lemma_text = lemma.find("l").get("t")
            for wordform in lemma.iter("f"):
                wordform_text = wordform.get("t")
                lemma_wordform_pairs.add((lemma_text.lower(), wordform_text.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_wordform_pairs, pickle_file)

        print("Extracted and saved lemma-wordform pairs.")

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения неуникальных пар лемма-словоформа из исходного XML-файла OpenCorpora.

        Проходит через XML-файл OpenCorpora и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        tree = ET.parse(self.data_path)
        root = tree.getroot()
        lemma_wordform_pairs = []

        for lemma in root.find("lemmata").iter("lemma"):
            lemma_text = lemma.find("l").get("t")
            for wordform in lemma.iter("f"):
                wordform_text = wordform.get("t")
                lemma_wordform_pairs.append((lemma_text.lower(), wordform_text.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_wordform_pairs, pickle_file)

        print("Extracted and saved not unique lemma-wordform pairs.")


class OpenCorporaCorpus(BaseDictionaryCorpus):
    def __init__(self, input_file, output_file, lemma_wordform_processor_class_name, data_path):
        """
        Инициализация класса OpenCorporaCorpus для работы с данными корпуса OpenCorpora.

        Args:
            data_path (str): Путь к исходным данным OpenCorpora (XML-файл корпуса OpenCorpora).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(input_file, output_file, lemma_wordform_processor_class_name, data_path)

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного XML-файла annot.opcorpora.xml

        Проходит через XML-файл OpenCorpora и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        root = ET.parse(self.data_path)

        lemma_word_pairs = set()

        for sentence in root.iter('sentence'):
            for token in sentence.iter('token'):
                # Проверяем, что у токена нет <g v="PNCT">
                if token.find('.//g[@v="PNCT"]') is None:
                    lemma_elems = token.findall('.//l[@t]')
                    if lemma_elems:
                        for lemma_elem in lemma_elems:
                            lemma = lemma_elem.get('t')
                            wordform = token.get('text')
                            lemma_word_pairs.add((lemma.lower(), wordform.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_word_pairs, pickle_file)

        print("Extracted and saved lemma-wordform pairs.")

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного XML-файла annot.opcorpora.xml

        Проходит через XML-файл OpenCorpora и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        # root = ET.parse("annot.opcorpora.xml")
        root = ET.parse(self.data_path)

        lemma_word_pairs = []

        for sentence in root.iter('sentence'):
            for token in sentence.iter('token'):
                # Проверяем, что у токена нет <g v="PNCT">
                if token.find('.//g[@v="PNCT"]') is None:
                    lemma_elems = token.findall('.//l[@t]')
                    if lemma_elems:
                        for lemma_elem in lemma_elems:
                            lemma = lemma_elem.get('t')
                            wordform = token.get('text')
                            lemma_word_pairs.append((lemma.lower(), wordform.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_word_pairs, pickle_file)

        print("Extracted and saved not unique lemma-wordform pairs from corpus.")


class Unimorph(BaseDictionaryCorpus):
    def __init__(self, data_path, input_file, output_file):
        """
        Инициализация класса OpenCorpora для работы с данными OpenCorpora.

        Args:
            data_path (str): Путь к исходным данным OpenCorpora (XML-файл словаря OpenCorpora).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(data_path, input_file, output_file)

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного txt-файла словаря unimorph.

        Проходит через файл и извлекает пары лемма-словоформа.

        Returns:
            None
        """

        # Открываем файл для чтения
        with open(self.data_path, 'r', encoding='utf-8') as file:
            # Создаем set для хранения уникальных пар лемма-словоформа
            unique_pairs = set()

            # Читаем строки файла
            for line in file:
                # Разделяем строку по символу табуляции
                parts = line.strip().split('\t')

                # Проверяем, что в строке есть три части
                if len(parts) == 3:
                    lemma, wordform, _ = parts  # Извлекаем лемму и словоформу

                    # Добавляем уникальные пары в set
                    unique_pairs.add((lemma.lower(), wordform.lower()))

        # Открываем файл для записи в бинарном режиме с использованием pickle
        with open(self.input_file, 'wb') as output_file:

            pickle.dump(unique_pairs, output_file)

        print("Extracted and saved lemma-wordform pairs.")


    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения неуникальных пар лемма-словоформа из исходного txt-файла словаря unimorph.

        Проходит через файл и извлекает пары лемма-словоформа.

        Returns:
            None
        """

        # Открываем файл для чтения
        with open(self.data_path, 'r', encoding='utf-8') as file:
            # Создаем set для хранения уникальных пар лемма-словоформа
            pairs = []

            # Читаем строки файла
            for line in file:
                # Разделяем строку по символу табуляции
                parts = line.strip().split('\t')

                # Проверяем, что в строке есть три части
                if len(parts) == 3:
                    lemma, wordform, _ = parts  # Извлекаем лемму и словоформу

                    # Добавляем уникальные пары в set
                    pairs.append((lemma.lower(), wordform.lower()))

        # Открываем файл для записи в бинарном режиме с использованием pickle
        with open(self.input_file, 'wb') as output_file:

            pickle.dump(pairs, output_file)

        print("Extracted and saved not unique lemma-wordform pairs.")


class UniversalDependenciesCorpus(BaseDictionaryCorpus):
    def __init__(self, input_file, output_file, lemma_wordform_processor_class_name, data_path):
        """
        Инициализация класса OpenCorporaCorpus для работы с данными корпуса SynTagRus.

        Args:
            data_path (str): Путь к исходным данным SynTagRus (папка SynTagRus, содержащая 5 файлов .conllu).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(data_path, input_file, output_file)

    def extract_lemma_wordform_pairs_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного conllu-файла

        Проходит по connlu-файлам папки SynTagRus и извлекает уникальные пары лемма-словоформа.

        Returns:
            None
        """

        lemma_word_pairs = set()
        # Получаем список файлов в указанной папке
        files = [f for f in os.listdir(self.data_path) if f.endswith('.conllu')]

        # Итерируемся по всем файлам в папке
        for file_name in files:

            file_path = os.path.join(self.data_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()

            sentences = parse(data)

            # Итерируемся по предложениям и извлекаем словоформы и леммы
            for sentence in sentences:
                for token in sentence:
                    # Проверяем, является ли токен пунктуацией
                    if token['upos'] != 'PUNCT':
                        # Извлекаем словоформу и лемму
                        wordform = token['form']
                        lemma = token['lemma']
                        lemma_word_pairs.add((lemma.lower(), wordform.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_word_pairs, pickle_file)

        print("Extracted and saved unique lemma-wordform pairs from SynTagRus corpus.")

    def extract_lemma_wordform_pairs_not_unique(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного conllu-файла

        Проходит по connlu-файлам папки SynTagRus и извлекает неуникальные пары лемма-словоформа.

        Returns:
            None
        """

        lemma_word_pairs = []

        # Получаем список файлов в указанной папке
        files = [f for f in os.listdir(self.data_path) if f.endswith('.conllu')]

        # Итерируемся по всем файлам в папке
        for file_name in files:

            file_path = os.path.join(self.data_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()

            # data_file = open(file_path, "r", encoding="utf-8")


            sentences = parse(data)

            # Итерируемся по предложениям и извлекаем словоформы и леммы
            for sentence in sentences:
                for token in sentence:
                    # Проверяем, является ли токен пунктуацией
                    if token['upos'] != 'PUNCT':
                        # Извлекаем словоформу и лемму
                        wordform = token['form']
                        lemma = token['lemma']
                        lemma_word_pairs.append((lemma.lower(), wordform.lower()))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_word_pairs, pickle_file)

        print("Extracted and saved not unique lemma-wordform pairs from SynTagRus corpus.")


# Пример использования
# opencorpora = OpenCorpora("dict.opcorpora_0_82.xml", "lemma_wordform_pair_last.pkl", "tree_set_new.pkl")
# opencorpora.extract_lemma_wordform_pairs_not_unique()
# opencorpora.build_trees()
# opencorpora.save_tree_set()

# unimorph = Unimorph("rus.txt", "pairs_from_unimorph_not_unique.pkl", "tree_set_from_unimorph_test.pkl" )
# unimorph.extract_lemma_wordform_pairs_not_unique()
# unimorph.build_trees()
# unimorph.save_tree_set()

# opencorporacorpus = OpenCorporaCorpus("annot.opcorpora.xml", config['OpenCorpora']['corpus'], config['OpenCorpora']['tree'])
# opencorporacorpus.extract_lemma_wordform_pairs_not_unique()
# opencorporacorpus.build_trees()
# opencorporacorpus.save_tree_set()

# unimorph = Unimorph("rus.txt", "pairs_Unimorph_not_unique.pkl", "ses_set_from_unimorph.pkl" )
# unimorph.extract_lemma_wordform_pairs_not_unique()
# unimorph.build_ses()
# unimorph.save_ses_set()

# syntagrus = SynTagRusCorpus(config['SynTagRus']['corpus'], "pairs_SynTagRus_corpus_not_unique.pkl ", config['SynTagRus']['trees'])
# syntagrus.extract_lemma_wordform_pairs_not_unique()
# syntagrus.build_trees()
# syntagrus.save_tree_set()
