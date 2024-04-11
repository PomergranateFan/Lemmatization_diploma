import pickle
import numpy as np

with open("syntagrus_f_x_dict.pkl", "rb") as f:
        f_x_data = pickle.load(f)

with open("tree_set_SynTagRus_corpus.pkl", 'rb') as f:
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
