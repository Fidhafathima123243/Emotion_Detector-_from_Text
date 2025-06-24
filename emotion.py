import pickle
import streamlit as st
import numpy as np

with open(r'C:\Users\fidha\Documents\Data_Science_Luminar\MAIN_PROJECTS\NLP\EMOTION_DETECTION\emotions.pkl','rb') as obj1:
    dict=pickle.load(obj1)

import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("EMOTION_DETECTION\emotion_wallpaper.jpg")

page_bg_img = f'''
<style>
.stApp {{
background-image: url("data:image/jpg;base64,{bg_img}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
image-rendering: auto;
background-colour: black;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# st.title('EmotionIQ: Decoding Human Feelings Through AI🤖❤️')
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: White;'> EmotionIQ: Decoding Human Feelings Through AI🤖❤️</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color: white;'>This tool uses AI to analyze text and detect the underlying emotion.</p>",
    unsafe_allow_html=True
)

vectorizer=dict['vectorizer']
le=dict['label']
model=dict['model']

st.markdown("""
    <style>
    textarea {
        background-color: #4B3832 !important; /* Espresso */
        color: #FFFFFF !important;
        caret-color: white !important; /*
        font-family: 'Segoe UI', sans-serif;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stTextArea label {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

user_input = st.text_area("Enter a sentence to receive a real-time emotion classification..")


if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Preprocess and predict
        vect_input = vectorizer.transform([user_input])
        pred = model.predict(vect_input)
        emotion = le.inverse_transform(pred)[0]

        st.success(f"Predicted Emotion: **{emotion}**")

