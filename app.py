import streamlit as st
import pandas as pd
import plotly.express as px

car_data= pd.read_csv('vehicles_us.csv')
st.header('Información de Vehículos')
hist_button = st.button('Construir histograma') # crear un botón
scat_button = st.button('Construir gráfico de dispersión')
     
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     
if scat_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig1 = px.scatter(car_data, x="odometer", y='price')
    st.plotly_chart(fig1, use_container_width=True)