import pandas as pd
import numpy as np

dataf = pd.DataFrame([
    ['John Smith','123 Main St',34],
    ['Jane Doe', '456 Maple Ave',28],
    ['Joe Schmo', '789 Broadway',51]
    ],
    columns=['name','address','age'])

dataf.set_index('name',inplace=True)

print(dataf)

df2 = pd.DataFrame({
            "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
})

print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.to_numpy())
print(df2.describe())

#pd.read_csv('data.csv')
#pd.read_excel('data.xlsx',sheet_name='Sheet1')
#pd.read_sql('SELECT * FROM data',connection_object)
#pd.read_json('https://api.github.com/users/hadley/orgs')
#pd.iloc[0] # first row of data frame
#pd.iloc[1] # second row of data frame
#pd.iloc[-1] # last row of data frame
#pd.columnName # select column by name
#pd['columnName'] # select column by name
#pd[['columnName1','columnName2']] # select two columns by name
#dataframe[dataframe.columnName.isin(['value1','value2'])] # filter by values
#dataframe.reset_index(drop=True) # reset index
#dataframe.reset_index(drop=True,inplace=True) # reset index in place, drop old index, modifies current dataframe
#dataframe.apply(function) # apply function to every row
#dataframe.apply(function,axis=1) # apply function to every column
#dataframe.column.command() - commands listed below until "unique"
#mean	Average of all values in column
#std	Standard deviation
#median	Median
#max	Maximum value in column
#min	Minimum value in column
#count	Number of values in column
#nunique	Number of unique values in column
#unique	List of unique values in column