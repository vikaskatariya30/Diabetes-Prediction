import streamlit as st
import pickle
import pandas as pd

def bmi_category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi>24.9:
        return "Normal weight"
    elif bmi>29.9:
        return "Overweight"
    else:
        return "Obese"

def bmi_category_column(bmi):
    if bmi=="Underweight":
        BMI_Category_Underweight=1
        BMI_Category_Obese=0
    else:
        BMI_Category_Underweight=0
        BMI_Category_Obese=1
    return BMI_Category_Underweight, BMI_Category_Obese

def age_group_column(age):

    if age >= 30 and age < 40:
        age_group_3040 = 1
        age_group_4050 = 0
        age_group_5060 = 0
        age_group_60 = 0
    elif age >= 40 and age < 50:
        age_group_3040 = 0
        age_group_4050 = 1
        age_group_5060 = 0
        age_group_60 = 0
    elif age >= 50 and age < 60:
        age_group_3040 = 0
        age_group_4050 = 0
        age_group_5060 = 1
        age_group_60 = 0
    else:
        age_group_3040 = 0
        age_group_4050 = 0
        age_group_5060 = 0
        age_group_60 = 1

    return age_group_3040, age_group_4050, age_group_5060, age_group_60

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title('Diabetes Prediction')

pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1, key='pregnancies')
glucose = st.number_input('Glucose', min_value=0.0, max_value=200.0, step=1.0, key='glucose')
blood_pressure = st.number_input('Blood Pressure', min_value=0.0, max_value=150.0, step=1.0, key='blood_pressure')
skin_thickness = st.number_input('Skin Thickness', min_value=0.000000, max_value=100.000000, step=1.000000, key='skin_thickness')
insulin = st.number_input('Insulin', min_value=0.000000, max_value=900.000000, step=1.000000, key='insulin')
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1, key='bmi')
bmi_category = bmi_category(bmi)
BMI_Category_Underweight, BMI_Category_Obese = bmi_category_column(bmi)
diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.000, max_value=2.500, step=0.010, key='diabetes_pedigree_function')
age = st.number_input('Age', min_value=0, max_value=120, step=1, key='age')
age_group_3040, age_group_4050, age_group_5060, age_group_60 = age_group_column(age)


scaler_data_frame = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, BMI_Category_Underweight, BMI_Category_Obese, diabetes_pedigree_function, age, age_group_3040, age_group_4050, age_group_5060, age_group_60]], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'BMI Category_Underweight', 'BMI Category_Obese', 'DiabetesPedigreeFunction', 'Age', 'Age_Group_30-40', 'Age_Group_40-50', 'Age_Group_50-60', 'Age_Group_60+'])

if st.button('predict'):
    scaled_data = scaler.fit_transform(scaler_data_frame)
    prediction = model.predict(scaled_data)
    st.write('The prediction is: {}'.format('Diabetic' if prediction[0] == 1 else 'Not Diabetic'))
