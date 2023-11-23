def longest_common_subsequence(x, y):
    """

    :param x: word 1
    :param y: word 2
    :return: longest common subsequence of word 1 and word 2
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)] # Cоздаем матрицу m+1 на n+1
    max_len = 0  # Для отслеживания длины наибольшей общей подпоследовательности
    end_index_x = 0  # Индекс окончания наибольшей общей подпоследовательности в строке x
    end_index_y = 0  # Индекс окончания наибольшей общей подпоследовательности в строке y

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index_x = i  # Обновляем индекс окончания при обнаружении более длинной подпоследовательности
                    end_index_y = j
            else:
                dp[i][j] = 0  # Обнуляем, если символы не совпадают

    if max_len == 0:
        return None  # Если наибольшей общей подпоследовательности нет, возвращаем None

    start_index_x = end_index_x - max_len  # Индекс начала наибольшей общей подпоследовательности в строке x
    start_index_y = end_index_y - max_len  # Индекс начала наибольшей общей подпоследовательности в строке y

    return (start_index_x, end_index_x, start_index_y, end_index_y)

x = "umgeschaut"
y = "umschauen"
result = longest_common_subsequence(x, y)
print(result)  # Должен вернуть (4, 9, 2, 7)
