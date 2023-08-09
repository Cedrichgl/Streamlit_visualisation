import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

sns.set_style('darkgrid')


st.title('Dashboard for autmated dataset')

def load_data():
    Df = pd.read_csv('/Users/hodewacedrichiheglo/Documents/Test/auto-mpg.csv')
    return Df

#load dataset
data = load_data()

Numeric_cols = data.select_dtypes(['float64','float32','int32','int64']).columns



Checkbox = st.sidebar.checkbox('Data reveal')
if Checkbox:
    st.dataframe(data=data)




#Add select widget
Select_box_one = st.sidebar.selectbox(label='X axis',options=Numeric_cols)
print(Select_box_one)
Select_box_two = st.sidebar.selectbox(label='Y axis',options=Numeric_cols)

#create scatterplot 
st.sidebar.subheader('Scatter plot')

sns.relplot(x=Select_box_one,y=Select_box_two,data=data,hue='origin')
st.pyplot()


#create histograms
st.sidebar.subheader('Histogram')
Select_box_three = st.sidebar.selectbox(label='Feature',options=Numeric_cols)
#Create histogram sliders
Histogram_slider = st.sidebar.slider(label='Number of bins',min_value=5,max_value=100,value=30)
sns.distplot(data[Select_box_three],bins=Histogram_slider)
st.pyplot()

