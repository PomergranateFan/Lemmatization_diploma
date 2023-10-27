def TREE_tuple(x, y):
    lcs_result = LCS(x, y)

    if lcs_result is None:
        return (x, y)
    else:
        i_s, i_e, j_s, j_e = lcs_result
        left_tree = TREE_tuple(x[:i_s], y[:j_s])
        right_tree = TREE_tuple(x[i_e:], y[j_e:])
        return (left_tree, i_s, right_tree, len(x) - i_e)
