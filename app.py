import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title('Diabetes Prediction')

pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1, key='pregnancies')
glucose = st.number_input('Glucose', min_value=0, max_value=200, step=1, key='glucose')
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=150, step=1, key='blood_pressure')
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1, key='skin_thickness')
insulin = st.number_input('Insulin', min_value=0, max_value=900, step=1, key='insulin')
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1, key='bmi')
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01, key='diabetes_pedigree_function')
age = st.number_input('Age', min_value=0, max_value=120, step=1, key='age')

scaler_data_frame = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

if st.button('predict'):
    scaled_data = scaler.fit_transform(scaler_data_frame)
    prediction = model.predict(scaled_data)
    st.write('The prediction is: {}'.format('Diabetic' if prediction[0] == 1 else 'Not Diabetic'))
