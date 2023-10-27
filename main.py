from Tree_function import TREE_tuple
from APPLY_function import APPLY

x = "umgeschaut"
y = "umschauen"
tree = TREE_tuple(x, y)
print(tree)
print(APPLY(tree, x))