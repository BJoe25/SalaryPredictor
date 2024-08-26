import streamlit as st
import pickle
import numpy as np

st.title("--Welcome to The Salary Predictor Web App--")

model = pickle.load(open('model.pkl', 'rb'))


col8 = st.columns(1)

with col8:
    st.markdown("<h1 style='text-align: center;'>Follow the steps below and click 'Predict Salary'</h1>", unsafe_allow_html = True)


gender_list = ["Male", "Female"]
education_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations",
            "Senior Data Scientist", "Senior Financial Analyst", 
            "Software Developer", "Sales Director", "Accountant",
            "Business Analyst", "Strategy Consultant", "Graphic Designer",
            "Supply Chain Manager", "Senior Consultant", "Network Engineer",
            "Project Manager", "Account Manager"]
job_index = [0, 1, 10, 11, 20, 4, 34, 5, 6, 3, 56, 65, 3, 21]

gender = st.radio('Gender: ', gender_list)
age = st.slider('Age: ', 21, 55)
education = st.selectbox('Education level: ', education_list)
job = st.selectbox('Job Title: ', job_list)
experience = st.slider('Years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

col12 = st.columns(5)

with col12:
    predict_button = st.button('Predict Salary')

if (predict_button):
    input1 = int(age)
    input2 = float(experience)
    input3 = int(job_index[job_list.index(job)])
    input4 = int(education_list.index(education))
    input5 = int(gender_list.index(gender))
    x = [input1, input2, input3, input4, input5]
    salary = model.predict([x])
    col16 = st.columns(3)

    with col16:
        st.text(f"Estimated Salary: ${int(salary[0])}")
