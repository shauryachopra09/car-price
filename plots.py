# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("visualise data")
  st.set_option("deprecation.showPyplotGlobalUse",False)
  st.subheader("scatter plot")
  features_list=st.multiselect("select x axis values",('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for i in features_list:
    st.subheader(f'scatter plot between {i} and price')
    plt.figure(figsize=(16,9))
    sns.scatterplot(x=i, y='price', data=car_df)
    st.pyplot()
  st.subheader("visualisation selector")
  plot_types=st.multiselect("select charts or plots", ("Histogram","Box Plot", "Correlation Heatmap"))
  if 'Histogram' in plot_types:
     st.subheader("Histogram")
     column=st.selectbox("select x axis values",('carwidth', 'enginesize', 'horsepower')) 
     st.title(f'histogram for {i}')
     plt.figure(figsize=(16,9))
     plt.hist(car_df[column], bins='sturges', edgecolor='red')
     st.pyplot() 
  if 'Box Plot' in plot_types:
     st.subheader("Box plot")
     column=st.selectbox("select x axis values",('carwidth', 'enginesize', 'horsepower')) 
     st.title(f'box plot for {i}')
     plt.figure(figsize=(16,9))
     sns.boxplot(car_df[column], orient='h')
     st.pyplot() 
  if 'Correlation Heatmap' in plot_types:
     st.subheader("Correlation Heatmap")
     plt.figure(figsize=(16,9))
     sns.heatmap(car_df.corr(), annot=True, cmap='gray')
     st.pyplot() 
    
    