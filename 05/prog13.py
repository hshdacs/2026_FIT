import numpy as np
import pandas as pd

# values = np.linspace(0, 1, 5)
# s = pd.Series(values)
# print(s)
# print(type(s))
# print(s[3])
# print(s.values)
# print(type(s.values))

# values = np.random.uniform(0,1, (4,3))
# columns = ['A', 'B', 'C']
# rows = pd.date_range("2026-11-04", periods=4)
# #print(values)
# df = pd.DataFrame(values, index=rows, columns=columns)
# print("Rohdaten:", df)

# df.sort_values(by="A", inplace=True)
# print("Sortierte Daten:", df)
# print(values)

# values = np.linspace(0, 1, 4)
# names = ["Alice", "Bob", "Charlie", "Dave"]
# intvalues = np.arange(5, 9, dtype="int32")
# index = ["A", "B", "C", "D"]
# data_dict = {
#     "Value": values,
#     "Name": names,
#     "Point": intvalues,
#     "Count": 1,
#     "Date": pd.Timestamp("2026-10-30")
# }

# df = pd.DataFrame(data_dict, index=index)
# print(df)
# print( df.describe() )
#print( df.head(2) )
#print( df.tail(2) )
#print( df.columns )
# print( df[ ["Date", "Name", "Value"] ] ) # Achtung, doppelte Klammer!
# print( df[["Date", "Name", "Value"]][1:3] )
# print( df[ df["Value"] < 0.5 ] )

# df["Neu"] = np.linspace(10, 11, 4)  # Neue Spalte hinzufügen
# df.at["B", "Point"] = 99            # Wert ändern
# df.iat[2, 3] = 17

# df.loc[:, "Date"] = pd.date_range("2026-12-01", periods=4)
# # oder per df.iloc[]

# print(df)
# df.to_csv("some_data.csv", index_label="Buchstabe")

df = pd.read_csv("some_data.csv", index_col="Buchstabe")
print(df)