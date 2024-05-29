import streamlit as st
import joblib
import numpy as np
from sklearn.tree import DecisionTreeRegressor

#_____________________________Variables
predict = 0

model = joblib.load('price_model.pkl')  

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



img_path = r'img\Casa-01.png'

#_____________________________________________SIDEBAR
with st.sidebar:
    with st.form('Variables', clear_on_submit=True):
        bedrooms =  st.selectbox("How many bedrooms?",
        ("1", "2", "3", "4"))
        bathrooms =  st.selectbox("How many bathrooms?",
        ("1", "2", "3",))
        stories =  st.selectbox("How many stories?",
        ("1", "2", "3", "4"))
        parking =  st.selectbox("How many parking spaces?",
        ("0","1", "2"))
        mainroad = st.checkbox("Mainroad")    
        guestroom = st.checkbox("Guestroom")    
        basement=   st.checkbox("Basement")
        hotwaterheating= st.checkbox("Hotwater heating")
        airconditioning= st.checkbox("Airconditioning")
        prefarea = st.checkbox("Preferred area")
        furnishingstatus = st.checkbox("Furnished")
        
        #Logaritmico        
        area = st.slider("Select house area(square foot):", 1650,16200,1650)
        "---"        
        submited = st.form_submit_button("Predict")
        
        if submited:
            # Convertir valores de checkboxes a enteros
            mainroad = int(mainroad)
            guestroom = int(guestroom)
            basement = int(basement)
            hotwaterheating = int(hotwaterheating)
            airconditioning = int(airconditioning)
            prefarea = int(prefarea)
            furnishingstatus = int(furnishingstatus)
            parking = int(parking)
            area = np.log(area)
            # Crear lista de valores para la predicción
            v_list = [int(bedrooms), int(bathrooms), int(stories), mainroad, guestroom, basement,
                      hotwaterheating, airconditioning, int(parking), prefarea, furnishingstatus, area]

            # Realizar la predicción
            w_pred = model.predict([v_list])
            predict = np.exp(w_pred)
            predict = int(predict)

            # Mostrar los resultados de la predicción
            st.session_state['predict'] = predict




#________________________________App

cl1, cl2, cl3 = st.columns([1,2,1])

with cl2:
    st.title('House value *STIMATOR*')
    "---"
    
    st.image(img_path)
    "---"    
    if 'predict' in st.session_state:
        
        st.subheader(f'House value prediction:')
        st.title(f'{st.session_state["predict"]}.00 $')
with cl3:
    st.subheader('House specifications')
    st.write(f'Bedrooms:    {bedrooms}')
    st.write(f'Bathrooms:   {bathrooms}')
    st.write(f'Stories:     {stories}')
    st.write(f'House area:   {round(np.exp(area),2)} sqf')



