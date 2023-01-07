import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.markdown("<h1 style='text-align: left; color: red;'>Welcome to Machine Learning Model Deployment</h1>", unsafe_allow_html=True)

add_selectbox2 = st.sidebar.selectbox(
     "Choose the dataset",
    ("Iris", "Cancer", "wine")
)
with open("git_iris/brain",'rb') as file:
    pred=pickle.load(file)

a = st.text_input("Sepal Length",0)
b = st.text_input("Sepal width",0)
c = st.text_input("petal length",0)
d = st.text_input("petal width",0)
try:
    a1=(float(a)-5.843333333333334)/0.828066127977863
    b1=(float(b)-3.0573333333333337)/0.4358662849366982
    c1=(float(c)-3.7580000000000005)/1.7652982332594662
    d1=(float(d)-1.1993333333333336)/0.7622376689603465
    result = pred.predict([[a1, b1, c1, d1]])
    st.markdown("<h2 style='text-align: left; color: red;'>Flower Name: </h1>",
                unsafe_allow_html=True)
    st.write(result[0])

except:
    st.write("please provide the proper value ")
