# Imports the libraries that are required
import streamlit as st
import pickle
import numpy as np

# Creates a title in streamlit
st.title("--Welcome to The Salary Predictor Web App--")

# Loads the model from the model.pkl file
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

# Creates three blank columns
col7, col8, col9 = st.columns(3)

# Blank column
with col7:
    st.write('')
# Markdown file that allows custom HTML/CSS styling in the web app. Here, a centered heading is created.
with col8:
    st.markdown("<h1 style='text-align: center;'>Follow the steps below and click 'Predict Salary'</h1>", unsafe_allow_html = True)
# Blank column    
with col9:
    st.write('')

# Creates a list of genders
gender_list = ["Male", "Female"]
# Creates a list of education levels
education_list = ["Bachelor's", "Master's", "PhD"]
# Creates a list of job titles
job_list = ["Director of Marketing", "Director of Operations",
            "Senior Data Scientist", "Senior Financial Analyst", 
            "Software Developer", "Sales Director", "Accountant",
            "Business Analyst", "Strategy Consultant", "Graphic Designer",
            "Supply Chain Manager", "Senior Consultant", "Network Engineer",
            "Project Manager", "Account Manager"]
# Creates a list of numbers corresponding to the job titles
job_index = [0, 1, 10, 11, 20, 4, 34, 5, 6, 3, 56, 65, 3,]

# For each case - The user's selection is stored in the respective variable
# Creates a radio button for gender
gender = st.radio('Gender: ', gender_list)
# Creates a slider for age - from 21 to 55
age = st.slider('Age: ', 21, 55)
# Creates a dropdown for education level
education = st.selectbox('Education level: ', education_list)
# Creates a dropdown for job titles 
job = st.selectbox('Job Title: ', job_list)
# Creates a slider for years of experience - from 0 to 25
experience = st.slider('Years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

# Creates five blank columns
col10, col11, col12, col13, col14 = st.columns(5)
# Blank column 
with col10:
    st.write('')
# Blank column 
with col11:
    st.write('')
# Column with a button for predicting salary
with col12:
    predict_button = st.button('Predict Salary')
# Blank column 
with col13:
    st.write('')
# Blank column 
with col14:
    st.write('')

# Checks if the button is pressed - When clicked the prediction process starts
if (predict_button):
# Converts the user's age to an integer
    input1 = int(age)
# Converts the user's years of experience to a float
    input2 = float(experience)
# Converts the job title into the corresponding number
    input3 = int(job_index[job_list.index(job)])
# Gets the index of the user's education
    input4 = int(education_list.index(education))
# Gets the index of the user's gender
    input5 = int(gender_list.index(gender))
# Stores the inputs into a list
    x = [input1, input2, input3, input4, input5]
# The model makes a salary prediction based on the inputs in the list; the prediction is stored in the salary variable
    salary = model.predict([x])

# Creates three blank columns
    col15, col16, col17 = st.columns(3)
# Blank column 
    with col15:
        st.write('')
# Column with textbox containing the predicted salary        
    with col16:
        st.text(f"Estimated Salary: ${int(salary[0])}")
# Blank column 
    with col17:
        st.write('')
