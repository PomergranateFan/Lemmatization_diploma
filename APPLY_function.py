def APPLY(tree, x):
    if isinstance(tree, tuple):
        if len(tree) == 4:
            tree_i, i_l, tree_j, j_l = tree
            i_l = int(i_l)
            j_l = int(j_l)

            if len(x) < i_l + j_l:
                return ""

            p = APPLY(tree_i, x[:i_l])  # Создаем префикс
            if p == None:
                return ""

            s = APPLY(tree_j, x[-j_l:])  # Создаем суффикс
            if s == None:
                return ""

            return p + x[i_l:len(x)-j_l] + s  # Конкатенируем префикс, LCS и суффикс

        elif len(tree) == 2:
            u, v = tree
            if x == u:
                return v
            else:
                return ""

    return None  # В случае неправильного формата дерева