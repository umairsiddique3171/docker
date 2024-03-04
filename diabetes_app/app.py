import streamlit as st
import pickle
import json
import numpy as np
from utils import classify, load_model , set_background


import warnings
warnings.filterwarnings("ignore")


# set background
set_background('background_img.jpg')


# set title
st.title("Diabetes Prediction Web App")


# getting input form user
col1, col2, col3 = st.columns(3)
    
with col1:
    pregnancies = st.text_input('Number of Pregnancies')
    
with col2:
    glucose = st.text_input('Glucose Level')

with col3:
    blood_pressure = st.text_input('Blood Pressure Value')

with col1:
    skin_thickness = st.text_input('Skin Thickness Value')

with col2:
    insulin = st.text_input('Insulin Value')

with col3:
    bmi = st.text_input('BMI Value')

with col1:
    dpf = st.text_input('DPF')

with col2:
    age = st.text_input('Age')


# load classifier
model = load_model("model.p")


# classification
if st.button('Results'):
    input_ref = ['Number of Pregnancies', 'Glucose Level', 'Blood Pressure Value', 'Skin Thickness Value', 'Insulin Value', 'BMI Value', 'DPF', 'Age']
    input_list = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    missing_values = [input_ref[i] for i, val in enumerate(input_list) if val is None or val == '']

    if missing_values:
        st.write("## Missing Values")
        for missing_value in missing_values:
            st.write(f"### '{missing_value}' missing.")
        st.write("## Please refresh and enter the values again")
    
    else: 
        results = classify([int(pregnancies),int(glucose),int(blood_pressure),int(skin_thickness),int(insulin),float(bmi),float(dpf),int(age)],model)
        classification = results['classification']
        score = results['score']

        # show results
        st.write("## Result")
        st.write(f"### Classification : {classification}")
        st.write(f"#### Confidence Score : {score}")

        