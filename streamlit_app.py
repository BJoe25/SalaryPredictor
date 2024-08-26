import streamlit as st
import pickle
import numpy as np

st.title("--Welcome to The Salary Predictor Web App--")

model = pickle.load(open('model.pkl', 'rb'))

# col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
# with col0:
#     st.write('')
# with col1:
#     st.write('')
# with col2:
#     st.write('')
# with col3:
#     st.title('wage')
# with col4:
#     st.write('')
# with col5:
#     st.write('')
# with col6:
#     st.write('')

col7, col8, col9 = st.columns(3)
with col7:
    st.write('')
with col8:
    st.markdown("<h1 style='text-align: center;'>Follow the steps below and click 'Predict Salary'</h1>", unsafe_allow_html = True)
with col9:
    st.write('')

gender_list = ["Male", "Female"]
education_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations",
            "Senior Data Scientist", "Senior Financial Analyst", 
            "Software Developer", "Sales Director", "Accountant",
            "Business Analyst", "Strategy Consultant", "Graphic Designer",
            "Supply Chain Manager", "Senior Consultant", "Network Engineer",
            "Project Manager", "Account Manager"]
job_index = [0, 1, 10, 11, 20, 4, 34, 5, 6, 3, 56, 65, 3,]

gender = st.radio('Gender: ', gender_list)
age = st.slider('Age: ', 21, 55)
education = st.selectbox('Education level: ', education_list)
job = st.selectbox('Job Title: ', job_list)
experience = st.slider('Years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')
with col12:
    predict_button = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

if (predict_button):
    input1 = int(age)
    input2 = float(experience)
    input3 = int(job_index[job_list.index(job)])
    input4 = int(education_list.index(education))
    input5 = int(gender_list.index(gender))
    x = [input1, input2, input3, input4, input5]
    salary = model.predict([x])
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')
    with col16:
        st.text(f"Estimated Salary: ${int(salary[0])}")
    with col17:
        st.write('')
