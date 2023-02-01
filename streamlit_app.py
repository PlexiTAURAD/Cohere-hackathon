import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

data = pd.DataFrame(
     np.random.randn(100,3),
  
  columns = ['a','b','c']




)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

pl.scatter(data['a'],data['b'])
pl.title('blah')
st.pyplot()

