import streamlit as st
import pandas as pd


st.set_page_config(
    layout="centered",
    page_title="Usando SelectBox, MultiSelects, File Uploader e Slider")

st.write("<h1><center>Usando SelectBox, MultiSelects, File Uploader e Slide</center><h1>", unsafe_allow_html=True)
st.subheader('Aula 7')

select = st.selectbox("Selecione uma cor:",("verde", "azul", "preto"))
st.write(f'Cor selecionada: {select}')

multi = st.multiselect("Selecione suas marcas:", ("bmw", "mercedes", "audi", "ferrari"))

st.write(f'Marcas selecionadas:')
for item in multi:
    st.write(item)

df = st.file_uploader('Selecione um arquivo excel:',type="xlsx")

if df:
    data = pd.read_excel(df)
    st.dataframe(data)