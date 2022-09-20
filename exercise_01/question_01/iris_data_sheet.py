
import pandas as pd

# read data
data = pd.read_csv(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# labeling columns
data.columns = ['Sepal length', 'Sepal width',
                'Petal length', 'Petal width', 'Class']

# this will print the first few rows
# print(data.head())


""" min_data = data["Sepal length"].min()
max_data = data["Sepal length"].max() """

# print("Minimum:", min_data, "\nMaximum:", max_data)


# print all the columns
""" for c in data.columns:
    print(c) """
