import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor

# Открываем файл для чтения
with open('tree_set_full.pkl', 'rb') as file:
    tree_set = pickle.load(file)

# Получаем количество элементов в объекте tree_set
num_elements = len(tree_set)
print(f"Количество элементов: {num_elements}")

# Закрываем файл
file.close()


