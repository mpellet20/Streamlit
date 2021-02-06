import pandas as pd
import numpy as np

DATA_URL = ("https://github.com/mpellet20/Streamlit/blob/main/fonds_fmoq.csv")

data = pd.read_csv(DATA_URL, nrows=nrows)

data = load_data(100000)
data
