import streamlit as st
import pandas as pd

st.title("Esto es un título")
st.header("Esto es un header")
st.markdown("*italic*")

df = pd.read_csv("C:/Users/samys/Documents/CienciaDatos/Programación para Análisis de Datos/src/streamlit/train.csv")
st.dataframe(df)
