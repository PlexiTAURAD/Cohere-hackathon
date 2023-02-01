import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

data = pd.DataFrame(
     np.random.randn(100,3),
  
  columns = ['a','b','c']




)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
chart = alt.Chart(data).mark_circle().encode(
x = 'a',y= 'b'


)
st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch
}
""")

data1 = pd.DataFrame({

T1 : ['Chic','min','lou']'
     'lat' : [41.868171, 44.979840, 38.257972, 39.030575],
     'lon' : [-87.667458,-93.272474,- 85.765187,-95.702548]









})


st.map(data1)
