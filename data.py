import numpy as np
import pandas as pd
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("view data")
  with st.expander("view data set"):
    st.table(car_df)
  st.subheader("columns description")
  if st.checkbox("show summary"):
    st.table(car_df.describe())
  col1, col2, col3=st.columns(3)
  with col1:
    if st.checkbox("show all column names"):
      st.table(list(car_df.columns))
  with col2:
    if st.checkbox("show all column data types"):
      st.table(car_df.dtypes)
  with col3:
    if st.checkbox("view column data"):
       column_data=st.selectbox("select columns", tuple(car_df.columns))
       st.write(car_df[column_data])