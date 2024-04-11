import pickle
import numpy as np

with open(config['SynTagRus']['dict'], "rb") as f:
        f_x_data = pickle.load(f)

with open(config['SynTagRus']['trees'], 'rb') as f:
    tree_set = pickle.load(f)

sum_x = 0
N = len(tree_set)
n=0
for x, info in f_x_data.items():
    f_x = info['f_x']
    sum_x += np.log(f_x)
    n+=1

result = sum_x/ N

print(result)

print(sum_x/n)
