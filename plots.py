import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def app(car_df):
  st.header('Visualize Data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('Scatter Plot')
  feature_list=st.multiselect('Select x-axis values',('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for i in feature_list:
    st.subheader(f'Scatter between {i} and price')
    plt.figure(figsize=(13,7))
    sns.scatterplot(x=i,y='price',data=car_df)
    st.pyplot()
  st.subheader('Visualization Selector')
  plt_types=st.multiselect('Select charts or plots',('Histogram','Boxplot','Correlation Heatmap'))
  if 'Histogram' in plt_types:
    st.subheader('Histogram')
    columns=st.selectbox('Select the columns to create histogram',('carwidth', 'enginesize', 'horsepower'))
    st.title(f'Histogram for {columns}')
    plt.figure(figsize=(13,7))
    plt.hist(car_df[columns],bins='sturges',edgecolor='red')
    st.pyplot()
  if 'Boxplot' in plt_types:
    st.subheader('Boxplot')
    column=st.selectbox('Select the columns to create boxplot',('carwidth', 'enginesize', 'horsepower'))
    st.title(f'Boxplot for {column}')
    plt.figure(figsize=(13,7))
    sns.boxplot(car_df[columns],orient='h')
    st.pyplot() 
  if 'Correlation Heatmap' in plt_types:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize=(8,8))
    sns.heatmap(car_df.corr(),annot=True,cmap='cubehelix')
    st.pyplot()