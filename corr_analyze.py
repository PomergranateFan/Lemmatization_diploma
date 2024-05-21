import pandas as pd

data = {
    'Корпус': ['gsd', 'gsd', 'gsd', 'poetry', 'poetry', 'poetry'],
    'Правило': ['tree', 'ud_with_copy', 'ud_without_copy', 'tree', 'ud_with_copy', 'ud_without_copy'],
    'K': [0.224, 0.006, 0.059, 0.253, 0.006, 0.054],
    'Точность лемматизации': [0.95638, 0.96000, 0.95904, 0.93215, 0.93823, 0.94022]
}

df = pd.DataFrame(data)

gsd_data = df[df['Корпус'] == 'gsd']
poetry_data = df[df['Корпус'] == 'poetry']

pearson_corr_gsd = gsd_data['K'].corr(gsd_data['Точность лемматизации'], method='pearson')
pearson_corr_poetry = poetry_data['K'].corr(poetry_data['Точность лемматизации'], method='pearson')

print("Коэффициент корреляции Пирсона для корпуса gsd:", pearson_corr_gsd)
print("Коэффициент корреляции Пирсона для корпуса poetry:", pearson_corr_poetry)


import matplotlib.pyplot as plt

# Scatter plot для корпуса gsd
plt.figure(figsize=(8, 6))
plt.scatter(gsd_data['K'], gsd_data['Точность лемматизации'], color='blue', label='gsd')
plt.title('Scatter Plot для корпуса gsd')
plt.xlabel('K')
plt.ylabel('Точность лемматизации')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot для корпуса poetry
plt.figure(figsize=(8, 6))
plt.scatter(poetry_data['K'], poetry_data['Точность лемматизации'], color='green', label='poetry')
plt.title('Scatter Plot для корпуса poetry')
plt.xlabel('K')
plt.ylabel('Точность лемматизации')
plt.legend()
plt.grid(True)
plt.show()