import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
st.header('Vendas de carros') # adicionar cabeçalho
hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button('Criar gráfico de dispersão') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Desenvolvento histograma referente a anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Desenvolvento gráfico de dispersão - Quilometragem vs Ano do modelo do carro')
    
    # criar um gráfito de dispersão
    fig = px.scatter(car_data, x="odometer", y="model_year")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True) 
