from suffix_trees import STree
import numpy as np
from typing import List, Tuple
import re



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

    def apply_rule(self, rule, x):
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
            left_tree = self.build_rule(x[:i_s], y[:j_s])
            right_tree = self.build_rule(x[i_e:], y[j_e:])
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

                s = self.apply_rule(tree_j, x[len(x)-j_l:])  # Создаем суффикс

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
                ses.append(('I', reversed_b[j - 1], len(reversed_a) - i))
                j -= 1
            else:
                i -= 1
                j -= 1

        return tuple(ses)
    def apply_rule(self, rule, x):
        word = list(x)
        # init_len = len(word)
        pos_dict = {}

        for i in range(len(word) + 2):
            pos_dict.update({i: i})

        for item in rule[::-1]:
            idx = pos_dict[item[2]]

            if item[0] == 'D':
                word[idx] = ' '
            elif item[0] == 'I':
                word.insert(idx, item[1])
                if item[2] < len(pos_dict):
                    for i in range(item[2] + 1, len(pos_dict)):
                        pos_dict.update({i: pos_dict[i] + 1})
                    pos_dict.update({len(pos_dict): pos_dict[len(pos_dict) - 1] + 1})

        word = "".join(word)


        return word.replace(' ', '')


class LemmaWordformProcessorUD(LemmaWordformProcessor):
    def __init__(self, allow_copy):
        """
        Конструктор класса LemmaWordformProcessorUD.
        """
        super().__init__()
        self.allow_copy = allow_copy
        pass

    def _min_edit_script(self, source, target, allow_copy):
        """
        Вычисляет минимальный скрипт редактирования для преобразования одной строки в другую.

        Параметры:
        - source: строка, исходная строка
        - target: строка, целевая строка
        - allow_copy: булево значение, разрешить ли копирование символов

        Возвращает строку, представляющую минимальный скрипт редактирования.
        """
        a = [[(len(source) + len(target) + 1, None)] * (len(target) + 1) for _ in range(len(source) + 1)]
        for i in range(0, len(source) + 1):
            for j in range(0, len(target) + 1):
                if i == 0 and j == 0:
                    a[i][j] = (0, "")
                else:
                    if allow_copy and i and j and source[i - 1] == target[j - 1] and a[i-1][j-1][0] < a[i][j][0]:
                        a[i][j] = (a[i-1][j-1][0], a[i-1][j-1][1] + "→")
                    if i and a[i-1][j][0] < a[i][j][0]:
                        a[i][j] = (a[i-1][j][0] + 1, a[i-1][j][1] + "-")
                    if j and a[i][j-1][0] < a[i][j][0]:
                        a[i][j] = (a[i][j-1][0] + 1, a[i][j-1][1] + "+" + target[j - 1])
        return a[-1][-1][1]

    def build_rule(self, form, lemma):
        """
        Генерирует правило лемматизации для заданной словоформы и ее леммы.

        Параметры:
        - form: строка, представляющая словоформу
        - lemma: строка, представляющая лемму
        - allow_copy: булево значение, разрешить ли копирование символов

        Возвращает строку, представляющую правило лемматизации.
        """
        form = form.lower()

        previous_case = -1
        lemma_casing = ""
        for i, c in enumerate(lemma):
            case = "↑" if c.lower() != c else "↓"
            if case != previous_case:
                lemma_casing += "{}{}{}".format("¦" if lemma_casing else "", case, i if i <= len(lemma) // 2 else i - len(lemma))
            previous_case = case
        lemma = lemma.lower()

        best, best_form, best_lemma = 0, 0, 0
        for l in range(len(lemma)):
            for f in range(len(form)):
                cpl = 0
                while f + cpl < len(form) and l + cpl < len(lemma) and form[f + cpl] == lemma[l + cpl]: cpl += 1
                if cpl > best:
                    best = cpl
                    best_form = f
                    best_lemma = l

        rule = lemma_casing + ";"
        if not best:
            rule += "a" + lemma
        else:
            rule += "d{}¦{}".format(
                self._min_edit_script(form[:best_form], lemma[:best_lemma], self.allow_copy),
                self._min_edit_script(form[best_form + best:], lemma[best_lemma + best:], self.allow_copy),
            )
        return rule

    def apply_rule(self, lemma_rule, form):
        """
        Применяет правило лемматизации к словоформе.

        Параметры:
        - form: строка, представляющая словоформу
        - lemma_rule: строка, представляющая правило лемматизации

        Возвращает лемматическую форму слова.
        """
        if ';' not in lemma_rule:
            raise ValueError('lemma_rule %r for form %r missing semicolon' %(lemma_rule, form))
        casing, rule = lemma_rule.split(";", 1)
        if rule.startswith("a"):
            lemma = rule[1:]
        else:
            form = form.lower()
            rules, rule_sources = rule[1:].split("¦"), []
            assert len(rules) == 2
            for rule in rules:
                source, i = 0, 0
                while i < len(rule):
                    if rule[i] == "→" or rule[i] == "-":
                        source += 1
                    else:
                        assert rule[i] == "+"
                        i += 1
                    i += 1
                rule_sources.append(source)

            try:
                lemma, form_offset = "", 0
                for i in range(2):
                    j, offset = 0, (0 if i == 0 else len(form) - rule_sources[1])
                    while j < len(rules[i]):
                        if rules[i][j] == "→":
                            lemma += form[offset]
                            offset += 1
                        elif rules[i][j] == "-":
                            offset += 1
                        else:
                            assert(rules[i][j] == "+")
                            lemma += rules[i][j + 1]
                            j += 1
                        j += 1
                    if i == 0:
                        lemma += form[rule_sources[0] : len(form) - rule_sources[1]]
            except:
                lemma = form

        for rule in casing.split("¦"):
            if rule == "↓0": continue # The lemma is lowercased initially
            if not rule: continue # Empty lemma might generate empty casing rule
            case, offset = rule[0], int(rule[1:])
            lemma = lemma[:offset] + (lemma[offset:].upper() if case == "↑" else lemma[offset:].lower())

        return lemma







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


