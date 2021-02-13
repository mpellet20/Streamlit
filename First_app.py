import streamlit as st

import numpy as np
import pandas as pd

#@st.cache(persist=TRUE)
def load_data(nrows):
    wind_data = pd.read_csv('WTG01.csv', nrows=nrows)
    return wind_data

wind_data = load_data(3170)

chart_data = wind_data.groupby('WIND_SPEED').AC_POWER.sum()

st.title('Here is the graphic of the AC_POWER related to the wind speed')

st.line_chart(chart_data)

if st.checkbox('Show Raw Data'):
    wind_data = load_data(10000)
    #wind_speed = st.slider('WIND_SPEED', 0, 23, 1)
    wind_date = st.slider('Date', '01/01/21', '23/01/2021',1)
    wind_data['Date'] = wind_date
    
    st.title('Data on Wind Power and Wind speed')
    st.write("Here's the data table: ")
    st.write(wind_data)

