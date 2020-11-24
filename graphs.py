import streamlit as st
import pandas as pd

df = pd.DataFrame({
  'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
  'second column': [10, 20, 30, 40]
})

df = df.rename(columns={'date':'index'}).set_index('index')

st.line_chart(df)
