import plotly.express as px
import random
import pickle
from lemma_wordform_processor import LemmaWordformProcessorSES
from collections import defaultdict
from config import config
class VisualizationProcessor:
    def __init__(self, lemma_wordform_processor, tree_file_path, pairs_file_path, output_file_path):
        """
        Конструктор класса для визуализации.

        :param lemma_wordform_processor: Экземпляр класса LemmaWordformProcessor для обработки лемм и словоформ.
        :param tree_file_path: Путь к файлу с деревьями.
        :param pairs_file_path: Путь к файлу с парами.
        :param output_file_path: Путь к файлу для сохранения результирующего словаря.
        """
        self.processor = lemma_wordform_processor()
        self.tree_file_path = tree_file_path
        self.pairs_file_path = pairs_file_path
        self.output_file_path = output_file_path

    @staticmethod
    def ddict2dict(d):
        """
        Метод для преобразования defaultdict в обычный словарь.

        :param d: defaultdict
        :return: Обычный словарь
        """
        for k, v in d.items():
            if isinstance(v, dict):
                d[k] = VisualizationProcessor.ddict2dict(v)
        return dict(d)

    def build_dictionary(self):
        """
        Метод для построения словаря по заданным файлам с деревьями и парами.
        Результат сохраняется в выходной файл.
        """
        with open(self.tree_file_path, 'rb') as f:
            tree_set = pickle.load(f)

        with open(self.pairs_file_path, 'rb') as f:
            pairs = pickle.load(f)

        result_dict = defaultdict(lambda: {'f_x': 0, 'trees': [], 'pairs': []})


        for tree in tree_set:
            x_counter = 0
            pairs_list = []

            for pair in pairs:

                lemma = self.processor.apply_rule(tree, pair[1])

                if lemma == pair[0]:
                    x_counter += 1

                    if len(pairs_list) < 5:
                        pairs_list.append(pair)

            result_dict[x_counter]['f_x'] += 1
            result_dict[x_counter]['trees'].append(tree)
            result_dict[x_counter]['pairs'].extend(pairs_list)

        result_dict_not_default = VisualizationProcessor.ddict2dict(result_dict)

        with open(self.output_file_path, 'wb') as output_file:
            pickle.dump(result_dict_not_default, output_file)

    def visualize(self):
        """
        Метод для визуализации данных из построенного словаря.
        """
        with open(self.output_file_path, 'rb') as f:
            result_dict = pickle.load(f)

        x_values = []
        y_values = []
        text_info = []

        for x_counter, values in result_dict.items():
            x_values.append(x_counter)
            y_values.append(values['f_x'])

            values['pairs'] = [pair for pair in values['pairs'] if ' ' not in pair[0]]
            random_pairs = random.sample(values['pairs'], min(3, len(values['pairs'])))
            pairs = []
            for lemma, wordform in random_pairs:
                tree = self.processor.build_rule(lemma, wordform)
                pairs.append((tree, lemma, wordform))
            random_pairs = pairs

            pair_info = '\n'.join([f"{pair}" for pair in random_pairs])
            text_info.append(f"\nPairs:\n{pair_info}")

        fig = px.scatter(x=x_values, y=y_values, hover_data={'text': text_info},
                         labels={'x': 'x', 'y': 'f_x'},
                         title='Частотный график построения леммы по словоформе')

        fig.update_xaxes(type='log')
        fig.update_yaxes(type='log')

        fig.show()

# Пример использования:
# processor = LemmaWordformProcessor()
# visualization_processor = VisualizationProcessor(processor, config['SynTagRus']['trees'],
#                                                  config['SynTagRus']['pairs'], 'str_f_x_correct_all.pkl')

# visualization_processor.build_dictionary()
# visualization_processor.visualize()
