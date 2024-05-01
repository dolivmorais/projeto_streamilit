import streamlit as st

st.header("Aula3 - Checkbox, Radio, Botões")
st.subheader("Em Aulas")

banho = st.checkbox("Banho")
escovar = st.checkbox("Escovar os dentes")

btn = st.button("Opinião")

if btn:
    if banho and escovar:
        st.success ("Banho e escovação estão ok, muito bem!!")
    elif banho is True and escovar is False:
        st.warning ("vai escovar os dentes!!")
    elif escovar is True and banho is False:
        st.warning ("precisa tomar banho!!")
    elif escovar is False and banho is False:
        st.warning ("Precisa tomar banho e escovar os dentes!!")

radio = st.radio("Cor favorita?", options=["azul","verde","amarelo"])

responder = st.button("Responder")

if responder:
    if radio == 'verde':
        st.success(f'você acertou')
    else:
        st.warning("você errou!!")