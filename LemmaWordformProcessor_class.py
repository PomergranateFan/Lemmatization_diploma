from suffix_trees import STree


class LemmaWordformProcessor:
    def __init__(self, lemma, wordform):
        """
        Конструктор класса LemmaWordformProcessor.

        Args:
            lemma (str): Лемма.
            wordform (str): Словоформа.
        """
        self.lemma = lemma
        self.wordform = wordform
        self.tree = None

    def set_tree(self, new_tree):
        """
        Метод для установки нового дерева.

        Args:
            new_tree (object): Новое дерево правил в формате tuple.
        """
        self.tree = new_tree

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

    def tree_method(self):
        """
        Метод для построения дерева на основе леммы и словоформы.
        """
        tree = self.build_tree(self.wordform, self.lemma)
        self.tree = tree

    def build_tree(self, x, y):
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
            left_tree = self.build_tree(x[:i_s], y[:j_s])
            right_tree = self.build_tree(x[i_e:], y[j_e:])
            return left_tree, i_s, right_tree, len(x) - i_e

    def get_tree(self):
        """
        Метод для получения дерева.

        Returns:
            object: Дерево правил в формате tuple.
        """
        return self.tree

    def apply(self, x):
        """
        Метод для применения дерева правил к словоформе и получения леммы.

        Args:
            x (str): Словоформа.

        Returns:
            str: Лемма.
        """
        if isinstance(self.tree, tuple):
            if len(self.tree) == 4:
                tree_i, i_l, tree_j, j_l = self.tree
                i_l = int(i_l)
                j_l = int(j_l)

                if len(x) < i_l + j_l:
                    return None

                self.tree = tree_i
                p = self.apply(x[:i_l])  # Создаем префикс
                if p is None:
                    return None

                self.tree = tree_j
                s = self.apply(x[-j_l:])  # Создаем суффикс
                if s is None:
                    return None

                return p + x[i_l:len(x) - j_l] + s  # Конкатенируем префикс, LCS и суффикс

            elif len(self.tree) == 2:
                u, v = self.tree
                if x == u:
                    return v
                else:
                    return None


'''
# Пример использования
lemma = "umschauen"
wordform = "umgeschaut"

processor = LemmaWordformProcessor(lemma, wordform)
processor.tree_method()
print(processor.get_tree())
result = processor.apply("umgeschaut")
print(f"Lemma: {result}")
'''



