import streamlit as st
import pandas as pd
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu
from PIL import Image
import pickle
import numpy as np
CURRENT_THEME = "blue"
IS_DARK_THEME = True
st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/artist-palette_1f3a8.png",
    width=100,
)

"""
# Try out Theming!

Click on the images below to view this app with different themes. 
"""

""

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER = "streamlit"

# Show thumbnails for available themes.
# As html img tags here, so we can add links on them.
cols = st.beta_columns(len(THEMES))
for col, theme in zip(cols, THEMES):

    # Get repo name for this theme (to link to correct deployed app)-
    if theme == "light":
        repo = "theming-showcase"
    else:
        repo = f"theming-showcase-{theme}"

    # Set border of current theme to red, otherwise black or white
    if theme == CURRENT_THEME:
        border_color = "red"
    else:
        border_color = "lightgrey" if IS_DARK_THEME else "black"

    col.markdown(
        #f'<p align=center><a href="https://share.streamlit.io/{GITHUB_OWNER}/{repo}/main"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        f'<p align=center><a href="https://apps.streamlitusercontent.com/{GITHUB_OWNER}/{repo}/main/streamlit_app.py/+/"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if theme in ["light", "dark"]:
        theme_descriptor = theme.capitalize() + " theme"
    else:
        theme_descriptor = "Custom theme"
    col.write(f"<p align=center>{theme_descriptor}</p>", unsafe_allow_html=True)


""
with st.beta_expander("Not loading?"):
    st.write(
        "You probably played around with themes before and overrode this app's theme. Go to ☰ -> Settings -> Theme and select *Custom Theme*."
    )
with st.beta_expander("How can I use this theme in my app?"):
    st.write(EXPANDER_TEXT)
selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Model","Contact"],
    icons = ["house","gear","envelope"],
    menu_icon = "cast",
    default_index = 0,
  )


#df = pd.read_csv("creditcard.csv")

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






