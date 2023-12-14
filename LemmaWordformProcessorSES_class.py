import numpy as np


class LemmaWordformProcessorSES:
    def __init__(self):
        """
        Конструктор класса лемма - словоформа процессора, основанного
        на статье Simple Data-Driven Context-Sensitive Lemmatization
        (Grzegorz Chrupała)
        """
        pass

    def find_ses(self, str_a, str_b):
        """
        Находит последовательность редактирования (SES) между двумя строками.

        :param str_a: Первая строка
        :param str_b: Вторая строка
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

        return ses

    def apply_ses(self, ses, word):
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


# Пример применения
# str_a = "pidieron"
# str_b = "pedir"

# processor = LemmaWordformProcessorSES()
# ses = processor.find_ses(str_a, str_b)
# print(processor.apply_ses(ses, str_a))
