import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/streamlit/train.csv")

#Creación de título con html
st.write("<h1 style='text-align: center; font-size: 3em;'>Visualización de datos Titanic</h1>", unsafe_allow_html=True)

#Histograma columna Survived
st.header("Sobrevivientes")
st.text("En el incidente hubo más personas que no sobrevivieron que las que sí")
hist_sobrevivientes, ax = plt.subplots()
survived = df["Survived"].value_counts()
ax.bar(survived.index, survived.values, color='#86bf91', width=0.5)
ax.set_xticks([0, 1])
ax.set_xticklabels(['No', 'Sí'])
ax.set_xlabel('Sobrevivió')
st.pyplot(hist_sobrevivientes)

#Histograma columna Pclass
st.header("Clase de pasajeros")
st.text("En el barco había más pasajeros que pertenecían a la clase 3 que a las otras dos.")
hist_clase, ax = plt.subplots()
clase = df["Pclass"].value_counts()
ax.bar(clase.index, clase.values, color='#e06666', width=0.5) 
ax.set_xticks([1, 2, 3]) 
ax.set_xticklabels(['1', '2', '3'])
ax.set_xlabel('Clase')
st.pyplot(hist_clase)

#Histograma columna Sex
st.header("Género de pasajeros")
st.text("En el barco había casi el doble de hombres que de mujeres")
hist_sexo, ax = plt.subplots()
clase = df["Sex"].value_counts()
ax.bar(clase.index, clase.values, color='#f1c232', width=0.5) 
ax.set_xticks([0,1]) 
ax.set_xticklabels(['Hombre', 'Mujer'])
ax.set_xlabel('Sexo')
st.pyplot(hist_sexo)

#Histograma columna Age
st.header("Edad de pasajeros")
st.text("La gran mayoría de pasajaeros estaban entre los 20 y 40 años de edad")
hist_edad, ax = plt.subplots()
clase = df["Age"].value_counts()
ax.bar(clase.index, clase.values, color='#b4a7d6', width=1) 
ax.set_xlabel('Edad')
st.pyplot(hist_edad)

#Histograma columna SibSp
st.header("Hermanos o pareja")
st.text("La gran mayoria de pasajeros iban solos o con un familiar en el barco")
hist_sibsp, ax = plt.subplots()
clase = df["SibSp"].value_counts()
ax.bar(clase.index, clase.values, color='#9fc5e8', width=0.5) 
ax.set_xlabel('Cantidad')
st.pyplot(hist_sibsp)

#Histograma columna Parch
st.header("Padres o niños")
st.text("La minoría de pasajeros eran padres o niños")
hist_parch, ax = plt.subplots()
clase = df["Parch"].value_counts()
ax.bar(clase.index, clase.values, color='#f6b26b', width=0.5) 
ax.set_xlabel('Cantidad')
st.pyplot(hist_parch)

#Histograma columna Fare
st.header("Precio de boleto")
st.text("La mayoría de los pasajeros del Titanic pagaron poco por su boleto, esto probablemente debido a que había más pasajeros que pertenecían a la tercera clase que a la segunda o primera.")
hist_fare, ax = plt.subplots()
clase = df["Fare"].value_counts()
ax.bar(clase.index, clase.values, color='#eb8aba', width=2) 
ax.set_xlabel('Precio')
st.pyplot(hist_fare)

#Histograma columna Cabin
st.header("Cabina de pasajeros")
st.text("Aunque hay muchos datos faltantes en esta categoría podemos observar que las cabinas estaban distribuidas sin tener mucha diferencia")
hist_cabin, ax = plt.subplots()
clase = df["Cabin"].value_counts()
ax.bar(clase.index, clase.values, color='#8bf266', width=0.5) 
ax.set_xlabel('Cabina')
st.pyplot(hist_cabin)

#Histograma columna Embarked
st.header("Lugares de embarcación")
st.text(" La gran mayoría de pasajeros embarcaron en  Southampton y la gran minoría en Queenstown")
hist_embarked, ax = plt.subplots()
clase = df["Embarked"].value_counts()
ax.bar(clase.index, clase.values, color='#ba3525', width=0.5) 
ax.set_xticks([0, 1, 2]) 
ax.set_xticklabels(['Southampton', 'Cherbourg', 'Queenstown'])
ax.set_xlabel('Embarcación')
st.pyplot(hist_embarked)
