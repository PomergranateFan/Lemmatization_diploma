from suffix_trees import STree
import numpy as np


class LemmaWordformProcessor:
    def __init__(self):
        """
        Конструктор класса LemmaWordformProcessor.
        """
        pass
    def build_rule(self, x, y):
        """
        Метод для построения дерева на основе леммы и словоформы.

        Args:
            x (str): Словоформа.
            y (str): Лемма.

        Returns:
            tuple: Правило
        """

        raise NotImplementedError("Метод должен быть реализован в подклассе!")

    def apply_rule(self, tree, x):
        """
        Метод для применения дерева правил к словоформе и получения леммы.

        Args:
            tree (tuple): Дерево разбора
            x (str): Словоформа.

        Returns:
            str: Лемма.
        """
        raise NotImplementedError("Метод должен быть реализован в подклассе!")






class LemmaWordformProcessorTree(LemmaWordformProcessor):
    def __init__(self):
        """
        Конструктор класса LemmaWordformProcessor.
        """
        super().__init__()
        pass

    def linear_longest_common_substring(self, x, y):
        """
        Метод для нахождения наибольшей общей подстроки в строках x и y.

        Args:
            x (str): Первая строка.
            y (str): Вторая строка.

        Returns:
            tuple: Кортеж с индексами начала и конца общей подстроки в строках x и y.
        """
        # Создаем обобщенное суффиксное дерево из двух строк
        stree = STree.STree([x, y])

        # Находим наибольшую общую подстроку
        lcs = stree.lcs()
        if not lcs:
            return None

        start_index_x = x.find(lcs)
        end_index_x = start_index_x + len(lcs)
        start_index_y = y.find(lcs)
        end_index_y = start_index_y + len(lcs)

        return start_index_x, end_index_x, start_index_y, end_index_y

    def build_rule(self, x, y):
        """
        Метод для построения дерева на основе леммы и словоформы.

        Args:
            x (str): Словоформа.
            y (str): Лемма.

        Returns:
            tuple: Дерево правил в формате tuple.
        """
        lcs_result = self.linear_longest_common_substring(x, y)

        if lcs_result is None:
            return x, y
        else:
            i_s, i_e, j_s, j_e = lcs_result
            left_tree = self.build(x[:i_s], y[:j_s])
            right_tree = self.build(x[i_e:], y[j_e:])
            return left_tree, i_s, right_tree, len(x) - i_e

    def apply_rule(self, tree, x):
        """
        Метод для применения дерева правил к словоформе и получения леммы.

        Args:
            tree (tuple): Дерево разбора
            x (str): Словоформа.

        Returns:
            str: Лемма.
        """
        if isinstance(tree, tuple):
            if len(tree) == 4:
                tree_i, i_l, tree_j, j_l = tree
                i_l = int(i_l)
                j_l = int(j_l)

                if len(x) < i_l + j_l:
                    return None

                p = self.apply_rule(tree_i, x[:i_l])  # Создаем префикс
                if p is None:
                    return None

                s = self.apply_rule(tree_j, x[-j_l:])  # Создаем суффикс
                if s is None:
                    return None

                return p + x[i_l:len(x) - j_l] + s  # Конкатенируем префикс, LCS и суффикс

            elif len(tree) == 2:
                u, v = tree
                if x == u:
                    return v
                else:
                    return None




class LemmaWordformProcessorSES(LemmaWordformProcessor):
    def __init__(self):
        """
        Конструктор класса лемма - словоформа процессора, основанного
        на статье Simple Data-Driven Context-Sensitive Lemmatization
        (Grzegorz Chrupała)
        """
        super().__init__()
        pass

    def build_rule(self, str_a, str_b):
        """
        Находит последовательность редактирования (SES) между двумя строками.

        :param str_a: Первая строка(слоформа)
        :param str_b: Вторая строка(лемма)
        :return: Список операций для приведения str_a к str_b
        """
        # Развернем строки для лучшей работы алгоритма
        reversed_a = str_a[::-1]
        reversed_b = str_b[::-1]

        # Заводим список с правилами редактирования (SES)
        ses = []

        # Создаем  матрицу для хранения расстояний редактирования
        dp = [[0] * (len(reversed_b) + 1) for _ in range(len(reversed_a) + 1)]

        # Заполняем матрицу расстояниями редактирования
        for i in range(len(reversed_a) + 1):
            for j in range(len(reversed_b) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif reversed_a[i - 1] == reversed_b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        # Обратный путь, чтобы найти SES
        i, j = len(reversed_a), len(reversed_b)
        while i > 0 or j > 0:
            if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                ses.append(('D', reversed_a[i - 1], len(reversed_a) - i))
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                ses.append(('I', reversed_b[j - 1], len(reversed_b) - j + 1))
                j -= 1
            else:
                i -= 1
                j -= 1

        return tuple(ses)

    def apply_rule(self, ses, word):
        """
        Применяет операции SES к данному слову.

        :param ses: Список операций SES
        :param word: Исходная словоформа
        :return: Модифицированное слово после применения операций SES
        """
        # Заводим копию слова
        word_copy = word

        # Создаем массив, хранящий позицию каждой буквы исходного слова в новом слове
        position_list = np.arange(len(word))

        for item in ses:
            if item[1] in word and len(word) + 1 > item[2]:
                index = position_list[item[2]]

                if item[0] == "D":
                    # Если встречаем операцию удалить, то индексы позиций после удаленной буквы
                    # уменьшаются на 1
                    my_array = np.zeros(len(word), dtype=position_list.dtype)
                    my_array[item[2] + 1:] = -1

                    position_list += my_array
                    word_copy = word_copy[:index] + word_copy[index + 1:]

                elif item[0] == "I":
                    # Если встречаем операцию вставить, то индексы позиций после вставленной буквы
                    # увеличиваются на 1

                    my_array = np.zeros(len(word), dtype=position_list.dtype)
                    my_array[item[2] + 1:] = 1
                    position_list += my_array
                    word_copy = word_copy[:index] + item[1] + word_copy[index:]

            else:
                return None

        return word_copy


'''
# Пример использования
lemma = "umschauen"
wordform = "umgeschaut"

processor = LemmaWordformProcessor()
tree = processor.build_tree(wordform, lemma)
result = processor.apply(tree, "umgeschaut")
print(f"Lemma: {result}")
print(tree)
'''


