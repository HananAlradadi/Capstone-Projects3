import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu
from PIL import Image
import pickle
import numpy as np

selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Model","Contact"],
    icons = ["house","gear","envelope"],
    menu_icon = "cast",
    default_index = 0,
  )

df = pd.read_csv("creditcard.csv")

filename = "final_model.sav"
model=pickle.load(open(filename, "rb"))


# PAGE 1
if selected == "Home":
    #st.title(f"You Have selected {selected}")
    st.markdown("<h1 style='text-align: center; color: black;'>Credit Card Fraud Detection App</h1>",
               unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
          img = Image.open("fraud-detection.png")
          st.image(img, width=300, use_column_width='auto')

    with col3:
        st.write(' ')

    st.markdown("<h4 style='text-align: center; color: gray;'>Stay one step ahead of fraudsters with our reliable transaction fraud detection solution.</h4>",
               unsafe_allow_html=True)
    
    #st.line_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)
  
if selected == "Model":
    st.markdown("<h1 style='text-align: center; color: black;'>Try our model:</h1>",
               unsafe_allow_html=True)

    form = st.form("my_form")

    V4 = form.slider('V4', -7.0, 17.0, 0.5)
    V10 = form.slider('V10', -25.0, 25.0, 0.5)
    V12 = form.slider('V12', -20.0, 9.0, 0.5)
    V14 = form.slider('V14', -20.0, 11.0, 0.5)
    V17 = form.slider('V17', -26.0, 11.0, 0.5)
    
    my_dict = {
        'V17':V17,
        'V14':V14,
        'V12':V12,
        'V10':V10,
        'V4':V4
    }

    df2 = pd.DataFrame.from_dict([my_dict])
    #st.table(df2)
    
    predict = form.form_submit_button("Predict")
    result = model.predict(df2)    
    result2 = model.predict_proba(df2)[:]
    if result > 0.5:
        st.markdown("<h4 style='color: green;'>Genuine Transaction.</h4>",
               unsafe_allow_html=True)
        s1 = "The probability of genuine transaction  % "  + str((result2[0][0].round(4) * 100 ).round(3))
        st.info(s1)
    else:
      st.markdown("<h4 style='color: red;'>Fraudulent Transaction</h4>",
               unsafe_allow_html=True)
      s1 = "The probability of fraudulent transaction  % "  + str((result2[0][1].round(4) * 100 ).round(3))
      st.info(s1)

if selected == "Contact":
    st.markdown("<h1 style='text-align: center; color: black;'>You can contact us through</h1>",
               unsafe_allow_html=True)
         
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
          img = Image.open("image.png")
          st.image(img, width=300, use_column_width='auto')

    with col3:
        st.write(' ')


    st.markdown("<h4 style='text-align: center; color: gray;'>Email: frauddetection@gmail.com</h4>",
               unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Phone Number: +966592748374</h4>",
               unsafe_allow_html=True)






