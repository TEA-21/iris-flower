import streamlit as st
import numpy as np
import pandas as pd

def app(car_df):
	st.header("View Data")
	with st.expander("View Dataset"):
		st.table(car_df)
	st.subheader("Columns Description:")
	if st.checkbox("Show summary"):
		st.table(car_df.describe())
	col1,col2,col3=st.columns(3)
	with col1:
		if st.checkbox("Show all columns names"):
			st.table(list(car_df.columns))
	with col2:
		if st.checkbox("View column datatype"):
			st.table(car_df.dtypes)
	with col3:
		if st.checkbox("View column data"):
			column_data=st.selectbox('Select Column',tuple(car_df.columns))
			st.write(car_df[column_data])