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