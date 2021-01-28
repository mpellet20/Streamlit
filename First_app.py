import streamlit as st

import numpy as np
import pandas as pd

s.t.write("Here's our first attempt at using data to create a table :")
st.write(pd.DataFrame({
      'First Column':[1, 2, 3, 4]
      'Second Column':[10, 20, 30, 40]
      }))
      
chart.data = pd.DataFrame(
         np.random.eandn(20, 3),
         columns=['a', 'b', 'c'])
         
st.line_chart(chart_data)

map_data = pd.DataFrame(
       np.random.randn(1000, 2) / [50, 50] + [37.76, -112.4],
       columns=['lat', 'lon'])
       
st.map(map_data)       
