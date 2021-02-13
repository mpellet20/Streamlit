import streamlit as st

import numpy as np
import pandas as pd

#@st.cache(persist=TRUE)
def load_data(nrows):
    wind_data = pd.read_csv('WTG01.csv', nrows=nrows)
    return wind_data

wind_data = load_data(10000)
wind_speed = 11
wind_data['WIND_SPEED'] = wind_speed
'data', wind_data


#wind_data = wind_data.wind_speed == wind_speed]

#, names=['Date', 'Time', 'AC_POWER', 'WIND_SPEED'])


st.title('Data on Wind Power and Wind speed')

st.write("Here's the data table: ")

st.write(wind_data)

#st.write('Here is the table of the Wind Speed related to the Wind Power')

#st.write(wind_data.groupby('AC_POWER').WIND_SPEED.sum())

#st.write('Here is the table of the wind speed related to the date')

#st.write(wind_data.groupby('Date').WIND_SPEED.sum())

chart_data = wind_data.groupby('WIND_SPEED').AC_POWER.sum()

st.title('Here is the graphic of the AC_POWER related to the wind speed')

st.line_chart(chart_data)

