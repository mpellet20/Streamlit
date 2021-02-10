# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:55:08 2021

@author: mpell
"""


import pandas as pd

wind_data = pd.read_csv('https://share.streamlit.io/mpellet20/streamlit/main/wtg01.csv', names=['Date','Time','AC_POWER','WIND_SPEED'])

#print(wind_data)

print(wind_data.groupby('AC_POWER').WIND_SPEED.sum())

print(wind_data.groupby('Date').WIND_SPEED.sum())

AC_POWER = wind_data.groupby('AC_POWER').WIND_SPEED.sum()
