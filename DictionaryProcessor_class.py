import pickle
import xml.etree.ElementTree as ET
from LemmaWordformProcessor_class import LemmaWordformProcessor
from LemmaWordformProcessorSES_class import LemmaWordformProcessorSES


class BaseDictionaryCorpus:
    def __init__(self, data_path, input_file, output_file):
        """
        Инициализация базового класса для работы с словарями и корпусами.

        Args:
            data_path (str): Путь к исходным данным (например, XML-файл словаря или корпуса).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        self.data_path = data_path
        self.input_file = input_file
        self.output_file = output_file
        self.tree_set = set()
        self.ses_set = set()
        self.processor = LemmaWordformProcessor()
        self.processor_ses = LemmaWordformProcessorSES()

    def build_trees(self):
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
            tree = self.processor.build_tree(wordform, lemma)
            self.tree_set.add(tree)

        file.close()

    def build_ses(self):
        """
        Метод для построения правил SES на основе пар лемма-словоформа.

        Проходит через пары лемма-словоформа и строит деревья с помощью LemmaWordformProcessorSES.

        Returns:
            None
        """
        with open(self.input_file, 'rb') as file:
            data = pickle.load(file)

        for pair in data:
            lemma, wordform = pair
            ses = self.processor_ses.find_ses(wordform, lemma)

            self.ses_set.add(ses)

        file.close()

    def save_tree_set(self):
        """
        Метод для сохранения деревьев в файл.

        Сохраняет построенные деревья в файл в формате pickle.

        Returns:
            None
        """
        with open(self.output_file, 'wb') as file:
            pickle.dump(self.tree_set, file)

    def save_ses_set(self):
        """
        Метод для сохранения правил SES в файл.

        Сохраняет построенные SES в файл в формате pickle.

        Returns:
            None
        """
        with open(self.output_file, 'wb') as file:
            pickle.dump(self.ses_set, file)


    def extract_lemma_wordform_pairs(self):
        """
        Метод для извлечения пар лемма-словоформа из исходного словаря.

        Проходит через файл и извлекает пары лемма-словоформа.

        Returns:
            None
        """
        raise NotImplementedError("Метод должен быть реализован в подклассе!")


class OpenCorpora(BaseDictionaryCorpus):
    def __init__(self, data_path, input_file, output_file):
        """
        Инициализация класса OpenCorpora для работы с данными OpenCorpora.

        Args:
            data_path (str): Путь к исходным данным OpenCorpora (XML-файл словаря OpenCorpora).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(data_path, input_file, output_file)

    def extract_lemma_wordform_pairs(self):
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
                lemma_wordform_pairs.add((lemma_text, wordform_text))

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
                lemma_wordform_pairs.append((lemma_text, wordform_text))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_wordform_pairs, pickle_file)

        print("Extracted and saved not unique lemma-wordform pairs.")


class OpenCorporaCorpus(BaseDictionaryCorpus):
    def __init__(self, data_path, input_file, output_file):
        """
        Инициализация класса OpenCorporaCorpus для работы с данными корпуса OpenCorpora.

        Args:
            data_path (str): Путь к исходным данным OpenCorpora (XML-файл корпуса OpenCorpora).
            input_file (str): Путь к файлу, в котором будут сохранены пары лемма-словоформа.
            output_file (str): Путь к файлу, в котором будут сохранены деревья.
        """
        super().__init__(data_path, input_file, output_file)

    def extract_lemma_wordform_pairs(self):
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
                            lemma_word_pairs.add((lemma, wordform))

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
        root = ET.parse("annot.opcorpora.xml")

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
                            lemma_word_pairs.append((lemma, wordform))

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

    def extract_lemma_wordform_pairs(self):
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
                    unique_pairs.add((lemma, wordform))

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
                    pairs.append((lemma, wordform))

        # Открываем файл для записи в бинарном режиме с использованием pickle
        with open(self.input_file, 'wb') as output_file:

            pickle.dump(pairs, output_file)

        print("Extracted and saved not unique lemma-wordform pairs.")


# Пример использования
# opencorpora = OpenCorpora("dict.opcorpora_0_82.xml", "lemma_wordform_pair_last.pkl", "tree_set_new.pkl")
# opencorpora.extract_lemma_wordform_pairs_not_unique()
# opencorpora.build_trees()
# opencorpora.save_tree_set()

# unimorph = Unimorph("rus.txt", "pairs_from_unimorph_not_unique.pkl", "tree_set_from_unimorph_test.pkl" )
# unimorph.extract_lemma_wordform_pairs_not_unique()
# unimorph.build_trees()
# unimorph.save_tree_set()

# opencorporacorpus = OpenCorporaCorpus("annot.opcorpora.xml", "pair_OpenCorpora_corpus.pkl", "tree_set_OpenCorpora_corpus.pkl")
# opencorporacorpus.extract_lemma_wordform_pairs_not_unique()
# opencorporacorpus.build_trees()
# opencorporacorpus.save_tree_set()

unimorph = Unimorph("rus.txt", "pairs_Unimorph_not_unique.pkl", "ses_set_from_unimorph.pkl" )
# unimorph.extract_lemma_wordform_pairs_not_unique()
unimorph.build_ses()
unimorph.save_ses_set()