import streamlit as st

import numpy as np
import pandas as pd

wind_data = pd.read_csv('WTG01.csv', names=['Date', 'Time', 'AC_POWER', 'WIND_SPEED'])

st.title('Data on Wind Power and Wind speed')

st.write("Here's the table related to the wind power:")

st.write(wind_data)

st.title('Here is the table of the Wind Speed related to the Wind Power')

st.write(wind_data.groupby('AC_POWER').WIND_SPEED.sum())

st.title('Here is the table of the wind speed related to the date')

st.write(wind_data.groupby('Date').WIND_SPEED.sum())

chart_data = wind_data.groupby('Date').WIND_SPEED.sum()

st.title('Here is the graphic of the wind speed related to the date')

st.line_chart(chart_data)
