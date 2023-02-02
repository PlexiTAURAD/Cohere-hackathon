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

'T1' : ['Chic'],
     

     'lat' : [13.124042],
     'lon' : [77.590924]









})


st.map(data1)
