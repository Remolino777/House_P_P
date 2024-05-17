import streamlit as st
import joblib
import numpy as np
from sklearn.tree import DecisionTreeRegressor

#_____________________________Variables

regression = joblib.load('price_model.pkl')

bedrooms =  1
bathrooms = 1
stories =   1
mainroad =  0
guestroom=  0
basement=   0
hotwaterheating= 0
airconditioning= 0
parking=    1
prefarea=   0
furnishingstatus=   0
area=   4753.029385188196

v_list = [bedrooms,bathrooms, stories, mainroad, guestroom, basement, hotwaterheating,
    airconditioning, parking, prefarea, furnishingstatus, area
]

img_path = r'img\Casa-01.png'


#________________________________App

cl1, cl2, cl3 = st.columns([1,2,1])

with cl2:
    "---"
    st.image(img_path)
    "---"
    st.subheader('Price prediction')
    


#_____________________________________________SIDEBAR
with st.sidebar:
    with st.form('Variables'):
        bedrooms =  st.selectbox("How many bedrooms?",
        ("1", "2", "3", "4"))
        bathrooms =  st.selectbox("How many bathrooms?",
        ("1", "2", "3",))
        stories =  st.selectbox("How many stories?",
        ("1", "2", "3", "4"))
        mainroad = st.checkbox("Mainroad")    
        guestroom = st.checkbox("Guestroom")    
        basement=   st.checkbox("Basement")
        hotwaterheating= st.checkbox("Hotwater heating")
        airconditioning= st.checkbox("Airconditioning")
        prefarea = st.checkbox("Preferred area")
        furnishingstatus = st.checkbox("Furnished")
        area = st.slider("Select house area(square foot):", 0,16200,0)
        "---"
        submited = st.form_submit_button("Submit")


