## Q1 Code Explanation:
###### line 2,3:
- 	import `pandas` for data analysis
- 	import `tabulate` for display data as a table

###### line 6:
- get data from **iris.data** file. (the file doesn't comes with column labels. try `print(data.head())` at line 7)

###### line 9:
- 	column labeling

###### line 13:
- 	create a dictionary (`data_dict`) store `min`, `max` data for relevant column

###### line 16 - 21:
- 	get first 4 columns (`data.columns[:4]`), then get the min and max value for each column, then append that values into `data_dict` ([Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries "Dictionary"))

###### line 24:
- 	create a table (more like a spreadsheet) from the dictionary 

###### line 27:
- 	print "Summary Statistics" row. [Padding and aligning strings](https://stackabuse.com/padding-strings-in-python/ "Learn more")

###### line 30:
- 	print rest of the table using [tabulate](https://pypi.org/project/tabulate/ "tabulate Doc").
