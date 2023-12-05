import pickle
import numpy as np
import matplotlib.pyplot as plt


with open('tree_numbers_counter_uniform.pkl', 'rb') as f:
    data = pickle.load(f)

# Вывод пар
# for tree, count in tree_counter.items():
#    print(f"Дерево: {tree}, Количество словоформ: {count}")


sum_keys = sum(data.keys())
sum_values = sum(data.values())

print(f"Сумма ключей: {sum_keys}")
print(f"Сумма значений: {sum_values}")

print(data)
np.seterr(divide='ignore')
# Разделение данных на x и f(x)
'''
x_values = np.array(list(data.keys()))
fx_values = np.array(list(data.values()))
# Преобразование x в логарифмическую шкалу
log_fx_values = np.log(fx_values)
log_x_values = np.log(x_values)
'''

# Построение scatter plot
plt.scatter( data.keys(), data.values(), label='log(f(x)) vs log(x)')
plt.yscale('log')
plt.xscale('log')
# Добавление подписей и легенды
plt.xlabel('log(x)')
plt.ylabel('log(f(x))')
plt.legend()

# Показ графика
plt.show()
