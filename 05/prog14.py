import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def datetime2fractional_year(date):
    year = date.year
    begin_of_year = dt.datetime(year, 1, 1)
    end_of_year = dt.datetime(year + 1, 1, 1)
    return year + ((date - begin_of_year).total_seconds() / ((end_of_year - begin_of_year).total_seconds()))

filename = "produkt_klima_tag_19530101_20201231_04931.txt"
raw_data = pd.read_csv(filename, sep=";")
#print(raw_data.tail(2))
# with pd.option_context("display.max_rows", 5, "display.max_columns", 8):
#     print(raw_data)
raw_data["MESS_DATUM"] = pd.to_datetime(raw_data["MESS_DATUM"].astype("str"), format="%Y%m%d")
#print(raw_data["MESS_DATUM"])

dfw = pd.DataFrame()
#dfw["year"] = raw_data["MESS_DATUM"].apply(datetime2fractional_year)
dfw["year"] = raw_data["MESS_DATUM"]
dfw["Temperature"] = raw_data[" TMK"]

#print(dfw)
#print(dfw.describe())

plt.plot( dfw["year"].values, dfw["Temperature"].values,
         '.', alpha=0.1, label="daily mean")
plt.xlabel("Year")
plt.ylabel("Temperature [°C]")
plt.legend()
plt.grid(visible=True, which="both", axis="both")
plt.show()
