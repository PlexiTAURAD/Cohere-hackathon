import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
     np.random.randn(100,3),
  
  columns = ['a','b','c']




)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
