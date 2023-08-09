import streamlit as st
import pandas as pd
import plotly.express as xp
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
sns.set_style("darkgrid")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.title('Uploader visualisation')
#fileuploader, Affichage du dataset aevc funct, affichage du describe, ajout des graphiques

st.sidebar.title('Visualisation de vos données')
Uploader = st.sidebar.file_uploader(label='Uploadez votre fichier',type=['csv','xlsx'])
#Df = pd.read_csv(Uploader)
if Uploader is not None:
    Df = pd.read_csv(Uploader)
else:
    st.warning("Vous devez d'abord importer votre fichier pour visualiser vos données")
Preview = st.sidebar.checkbox('Afficher votre dataset')
if Preview:
    st.write(Df)
    st.write(Df.shape)
    Describe = st.sidebar.checkbox('Les statistiques de votre dataset')
    if Describe:
        st.write(Df.describe())

#les types de données
def Data():
    Col_num = Df.select_dtypes(['int','float']).columns
    Col_str = Df.select_dtypes(['object']).columns
    return Col_num,Col_str


Num_cols = Df.select_dtypes(['float','int']).columns

#Add select widget and menu 

Choice = ['Scatter','Histograme','Camenbert']
Menu = st.sidebar.selectbox(label='Choisissez votre graph',options=Choice)

if Menu == 'Scatter':
    Select_X = st.sidebar.selectbox(label='Votre variable X',options=Num_cols)
    Select_Y =st.sidebar.selectbox(label='Votre variable Y',options=Num_cols)
#create scatter plot
    st.sidebar.subheader('Scatter plot')
    sns.relplot(data=Df,x=Select_X, y=Select_Y)
    st.pyplot()
elif Menu == 'Histogramme':
    #create histogram
    st.sidebar.subheader('Histogramme')
    Select_three = st.sidebar.selectbox(label='Variables',options=Num_cols)
    Histogram_slider = st.sidebar.slider(label='Tranches',min_value=5,max_value=100,value=30)
    sns.distplot(Df[Select_three],bins=Histogram_slider)
    st.pyplot()
else:
    st.sidebar.subheader('Pie chart')
    Select_foor = list(Df.select_dtypes(['object']).columns)
    st.write(Select_foor)
    plt.pie(Select_foor,labels=Select_foor.index,shadow=True,autopct='%1.1f%%')
    
