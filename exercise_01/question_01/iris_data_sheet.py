
import pandas as pd
from tabulate import tabulate

# read data
data = pd.read_csv('./iris.data')

# labeling columns 
data.columns = ['Sepal length', 'Sepal width',
                'Petal length', 'Petal width', 'Class']

# empty dictionary 
data_dict = {" ": [], "Min": [], "Max": []}

# fill data to 'data_dict'
for c in data.columns[:4]:
    min = data.loc[data[c].idxmin()]
    max = data.loc[data[c].idxmax()]
    data_dict[' '].append(c)
    data_dict['Min'].append(f'{min[c]} ({min["Class"].split("-")[1]})')
    data_dict['Max'].append(f'{max[c]} ({max["Class"].split("-")[1]})')

# make dictionary to DataFrame
df = pd.DataFrame(data_dict)

# print "Summary Statistics" row 
print("{}\n|{:>35}{:>17}".format(f'+{"-"*51}+',"Summary Statistics", "|"))

# print rest of the table 
print(tabulate(df, headers='keys', tablefmt='grid',
               showindex=False, colalign=("left", "left", "left")))
