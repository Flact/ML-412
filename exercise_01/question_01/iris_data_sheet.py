
import pandas as pd
# from tabulate import tabulate

# read data
data = pd.read_csv(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# labeling columns
data.columns = ['Sepal length', 'Sepal width',
                'Petal length', 'Petal width', 'Class']

# this will print the first few rows
# print(data.head())

# print(data)

""" min_data = data["Sepal length"].min()
max_data = data["Sepal length"].max() """

# print("Minimum:", min_data, "\nMaximum:", max_data)


# print all the columns
for c in data.columns[:4]:
    min = data.loc[data[c].idxmin()]
    max = data.loc[data[c].idxmax()]
    print(f'{c} \t {min[c] :<6} ({min["Class"].split("-")[1]})\t\
        {max[c]} ({max["Class"].split("-")[1]})')
