#%%
import streamlit as st
import pandas as pd
#%%
st.set_page_config(
    page_title="Aula 5",
    page_icon="🔴"
)

st.write('# Bem vindo a aula 5 🔴 ')
#%%
caminho_darquivo0 = './planilha_vendas.csv'
caminho_darquivo1 = './dados_teste.csv'
df0 = pd.read_csv(caminho_darquivo0)
df1 = pd.read_csv(caminho_darquivo1)
st.dataframe(df0)
st.dataframe(df1)
# st.write('outra forma ...')
# st.table(df1)
