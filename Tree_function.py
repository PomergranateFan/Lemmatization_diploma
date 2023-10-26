def TREE(x, y):
    lcs_result = LCS(x, y)  # Получаем результат LCS

    if lcs_result is None:
        # Если LCS вернула None, это означает отсутствие общей подпоследовательности
        return f"SUB({x}, {y})"
    else:
        i_s, i_e, j_s, j_e = lcs_result  # Извлекаем индексы начала и конца LCS
        left_tree = TREE3(x[:i_s], y[:j_s])
        right_tree = TREE3(x[i_e:], y[j_e:])
        return f"({left_tree}, ({i_s}, {len(x) - i_e}), {right_tree})"
