import streamlit as st
from funcs import check_email,plot_body_fat,calculate_metrics


st.write("Welcome to BMI/Body fat calculator")

with st.form("Please enter your data:"):
    name = st.text_input(label="Name:")
    email = st.text_input(label="Email:")
    age  = st.number_input(label="Age",step=1,min_value=1,max_value=130)
    height = st.number_input(label="Height:",step=0.01,min_value = 1.00,max_value = 3.00)
    weight = st.number_input(label = "Weight:",step=0.01,min_value = 10.00,max_value = 300.00)
    gender = st.radio("Gender:",("Male","Female"))
    submitted = st.form_submit_button(label = "Calculate")
    if submitted:
        email_true = check_email(name,email)    
        if not email:
            st.write("Check your email:")
        else:
            bmi,body_fat = calculate_metrics(age,height,weight,gender)
            st.write(f"Your Body Mass Index is: {bmi:.2f}")
            st.write(f"Your Body fat percentage is: {body_fat:.2f}")
            st.pyplot(plot_body_fat(body_fat))
    