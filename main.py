import pandas as pd

# Загрузить датасет из файла
dataset = pd.read_csv('Dota2 Heroes by MMR Bracket.csv')

# Вывести весь датасет
print(dataset)

# Описание датасета
print(dataset.describe())

# Размерность массива (количество строк, количество столбцов)
print(dataset.shape)

# Наименование колонок
print(dataset.columns)

# Уникальные значения в каждом столбце
print(dataset.nunique())

# Сортировка по столбцу 'Heroes'
sorted_df = dataset.sort_values('Heroes')

# Удаление столбцов '(>2K MMR) KDA Ratio' и '(>2K MMR) Avg Match'
df = sorted_df.drop(['(>2K MMR) KDA Ratio', '(>2K MMR) Avg Match'], axis=1)

# Удаление строк с пустыми значениями
df = df.dropna()

# Замена пустых значений на 0
df = df.replace('', 0)

# Удаление дубликатов
df = df.drop_duplicates()

# Вывод информации о DataSet
df.info()

# Вывод описательной статистики DataSet
df.describe()

# Удаление символов процента из столбца
df['(<2K MMR) WinRate(%)'] = df['(<2K MMR) WinRate(%)'].str.rstrip('%')

# Преобразование столбца в числовой формат
df['(<2K MMR) WinRate(%)'] = pd.to_numeric(df['(<2K MMR) WinRate(%)'], errors='coerce')

# Выборка данных по строкам и столбцам
selected_data = df.loc[df['(<2K MMR) WinRate(%)'] > 5, ['(2K-3K MMR) PickRate(%)', '(<2K MMR) WinRate(%)']]



# Сохранение нового датасета в CSV формате
df.to_csv('NewDota2 Heroes by MMR Bracket.csv', index=False)
