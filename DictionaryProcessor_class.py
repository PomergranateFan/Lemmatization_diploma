import pickle
import xml.etree.ElementTree as ET
from LemmaWordformProcessor_class import LemmaWordformProcessor

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

    def build_trees(self):
        """
        Метод для построения деревьев на основе пар лемма-словоформа.

        Проходит через пары лемма-словоформа и строит деревья с помощью LemmaWordformProcessor.

        Returns:
            None
        """
        with open(self.input_file, 'rb') as file:
            data = pickle.load(file)

        for i, pair in enumerate(data[:200]):
            lemma, wordform = pair
            processor = LemmaWordformProcessor(lemma, wordform)
            processor.TREE()
            self.tree_set.add(processor.get_tree())

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
        lemma_wordform_pairs = []

        for lemma in root.find("lemmata").iter("lemma"):
            lemma_text = lemma.find("l").get("t")
            for wordform in lemma.iter("f"):
                wordform_text = wordform.get("t")
                lemma_wordform_pairs.append((lemma_text, wordform_text))

        with open(self.input_file, "wb") as pickle_file:
            pickle.dump(lemma_wordform_pairs, pickle_file)

        print("Extracted and saved lemma-wordform pairs.")

# Пример использования
opencorpora = OpenCorpora("dict.opcorpora_0_82.xml", "lemma_wordform_pair_new_test.pkl", "tree_set_new_test.pkl")
opencorpora.extract_lemma_wordform_pairs()
opencorpora.build_trees()
opencorpora.save_tree_set()
