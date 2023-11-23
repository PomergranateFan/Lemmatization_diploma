import pickle
from LemmaWordformProcessor_class import LemmaWordformProcessor
'''

# Открываем файл для чтения
with open('tree_set_new_test.pkl', 'rb') as file:
    tree_set = pickle.load(file)

# Выводим первые 10 объектов
for i, tree in enumerate(tree_set):
    if i < 10:
        print(f"Object {i + 1}: {tree}")
    else:
        break

# Закрываем файл
file.close()

'''
x = "Козел"
y = "Козла"

processor = LemmaWordformProcessor(x, y)
processor.TREE()
print(processor.get_tree())

result = processor.APPLY("ежа")
print(f"Lemma: {result}")

