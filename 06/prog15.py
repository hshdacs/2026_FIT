import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

url = "https://api.openweathermap.org/data/2.5/weather?q=Heidelberg,de&APPID=8903a345e1b9134f8001e71b8748a08f"
raw_data = pd.read_json(url)
print(raw_data)

