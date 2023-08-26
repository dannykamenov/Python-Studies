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
#dataframe.groupby('columnName').mean() # get mean of each column with unique values of columnName
#dataframe.groupby(['columnName1','columnName2']).mean() # get mean of each column with unique values of columnName1 and columnName2
#dataframe.pivot(index='columnName',columns='columnName2',values='columnName3') # create pivot table that groups by columnName1 and calculates the mean of columnName2 and columnName3
#dataframe.groupby('columnName').agg(np.mean) # find the average across all columns for every unique columnName
#dataframe['column] = dataframe['column'].astype(float) # convert the datatype of the series to float
#dataframe['column'] = pd.Categorical(dataframe['column'], [1,2,3,4], ordered=True) # convert the datatype of the series to categorical with ordering
#dataframe.sort_values('column1') # sort values by column1 in ascending order
#dataframe.sort_values('column2',ascending=False) # sort values by column2 in descending order
#dataframe.sort_values(['column1','column2'],ascending=[True,False]) # sort values by column1 in ascending order then column2 in descending order
#dataframe['column1'].unique() # get unique values in column1
#dataframe['column1'].nunique() # get number of unique values in column1
#dataframe['column1'].value_counts() # get number of times each value in column1 occurs
#dataframe['column1'].value_counts(normalize=True) # get percentage of times each value in column1 occurs
#dataframe['column1'].apply(function) # apply function to values in column1
#dataframe['column1'].apply(lambda x: x*2) # apply function to values in column1
#dataframe.dropna() # drop all rows that contain null values
#dataframe.dropna(axis=1) # drop all columns that contain null values
#dataframe.dropna(axis=1,thresh=n) # drop all rows have have less than n non null values
#dataframe.fillna(x) # replace all null values with x
#dataframe['column1'].fillna(dataframe['column1'].mean()) # replace all null values in column1 with the mean of column1
#dataframe.duplicated() # returns true for every row that is a duplicate, false otherwise
#dataframe.drop_duplicates() # drop all duplicate rows
#dataframe.drop_duplicates(['column1','column2']) # drop all duplicate rows based on column1 and column2
#dataframe.rename(columns={'oldName1':'newName1','oldName2':'newName2'}) # rename columns
#dataframe.set_index('column1') # change the index
#dataframe.rename(index={0:'firstEntry',1:'secondEntry'}) # rename index
#dataframe.rename(index=str.lower) # change the index to lowercase
#dataframe.rename(columns=str.lower) # change the column names to lowercase
#pd.concat([dataframe1,dataframe2,dataframe3]) # concatenate dataframes together in order
#pd.concat([dataframe1,dataframe2,dataframe3],axis=1) # concatenate dataframes together in order
#dataframe1.append(dataframe2) # append dataframe2 to dataframe1
#dataframe1.append(dataframe2,ignore_index=True) # append dataframe2 to dataframe1 and reset the index
#dataframe.join(dataframe2,on='column1',how='inner') # SQL-style join the columns in dataframe1 and dataframe2
#dataframe.merge(dataframe2,on='column1') # merge dataframe1 and dataframe2 together
#dataframe.merge(dataframe2,left_on='column1',right_on='column2') # merge dataframe1 and dataframe2 together
#dataframe.pivot_table(index='column1',values='column2',aggfunc=np.mean) # create pivot table that groups by column1 and calculates the mean of column2
#dataframe.pivot_table(index='column1',values='column2',aggfunc=np.mean,columns='column3') # create pivot table that groups by column1 and calculates the mean of column2 and column3
#dataframe.groupby('column1').agg(np.mean) # find the average across all columns for every unique column1
#dataframe.apply(np.mean) # apply the function np.mean() across each column
#dataframe.apply(np.max,axis=1) # apply the function np.max() across each row
#dataframe.apply(lambda x: x.max() - x.min()) # apply the function x.max() - x.min() across each column
#dataframe['column1'].apply(lambda x: 1 if x > 0 else 0) # apply the function x > 0 ? 1 : 0 across each value in column1
#scipy - trim_mean(dataframe['column1'],0.1) # trim the mean of column1 by 10%
#dataframe.column.max() # find the max of column
#dataframe.column.min() # find the min of column
#dataframe.column.quantile(0.25) # find the 25th percentile of column
#scipy - stats.iqr(dataframe.column) # find the interquartile range of column
#dataframe.column.var() # find the variance of column
#dataframe.column.std() # find the standard deviation of column
#dataframe.column.mad() # find the mean absolute deviation of column
#dataframe.column.skew() # find the skewness of column
#seaborn as sns - sns.boxplot(x='column1',y='column2',data=dataframe) # create a boxplot of column1 and column2
#seaborn as sns - sns.histplot(dataframe.column1,kde=False) # create a histogram of column1
#seaborn as sns - sns.distplot(dataframe.column1,kde=False) # create a histogram of column1
#seaborn as sns - sns.distplot(dataframe.column1) # create a histogram of column1
#seaborn as sns - sns.countplot(x='column1',data=dataframe) # create a histogram of column1
#dataframe.column.value_counts().plot().pie() # create a pie chart of column1
#plt.hist(dataframe.column1, color='something',label='something',normed=True//renamed to density) # create a histogram of column1