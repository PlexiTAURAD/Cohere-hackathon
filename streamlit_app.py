import streamlit as st
import pandas as pd
import numpy as np

A = [1,2,3,4,5,6,7,8]
n = np.array(A)
nd = n.reshape((2,4))

st.table(A)
