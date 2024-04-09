import streamlit as st
import pandas as pd
import numpy as np
import pickle

html_temp = """
<div style="background-color:yellow;padding:1.5px">
<h1 style="color:black;text-align:center;">Used Car Price Prediction</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)

filename = 'Auto_Price_Pred_Model.pkl'  # Correct the filename extension to '.pkl'
model = pickle.load(open(filename, 'rb'))

with st.sidebar:
    st.subheader('Car Specs to Predict Price')
    make_model = st.selectbox("Model Selection", ("Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"))
    hp_kW = st.number_input("Horse Power:", min_value=40, max_value=294, value=120, step=5)
    age = st.number_input("Age:", min_value=0, max_value=3, value=0, step=1)
    km = st.number_input("km:", min_value=0, max_value=317000, value=10000, step=5000)
    Gears = st.number_input("Gears:", min_value=5, max_value=8, value=5, step=1)
    Gearing_Type = st.radio("Gearing Type", ("Manual", "Automatic", "Semi-automatic"))

my_dict = {"make_model": make_model, "hp_kW": hp_kW, "age": age, "km": km, "Gears": Gears, "Gearing_Type": Gearing_Type}
df = pd.DataFrame.from_dict([my_dict])

cols = {
    "make_model": "Car Model",
    "hp_kW": "Horse Power",
    "age": "Age",
    "km": "km Traveled",
    "Gears": "Gears",
    "Gearing_Type": "Gearing Type"
}

df_show = df.rename(columns=cols)  # Use the rename method to rename the columns
st.write("Selected Specs:")
st.table(df_show)

if st.button("Predict"):
    pred = model.predict(df)
    st.write("The estimated value of car price is €", int(pred[0]))

