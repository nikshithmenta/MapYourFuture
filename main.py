import streamlit as st
import pandas as pd
import numpy as np 
import pickle

@st.cache_resource

def load_model():
    with open('knn_model.pkl', 'rb') as file:
        loaded_ml_model = pickle.load(file)
    return loaded_ml_model
# data1=dict()
st.set_page_config(layout="wide", page_title='Map Your Future')

st.header('Map Your Future') 

model_1 = load_model() 

col1, ecol, col2 = st.columns([1.5, 0.2, 1.5])

with col1:
    q1 = st.selectbox('Database Fundamentals :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q2 = st.selectbox('Computer Architecture :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q3 = st.selectbox('Distributed Computing Systems :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q4 = st.selectbox('Cyber Security :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q5 = st.selectbox('Networking :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q6 = st.selectbox('Software Development :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q7 = st.selectbox('Programming Skills :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q8 = st.selectbox('Project Management :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q9 = st.selectbox('Computer Forensics Fundamentals :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
with col2 :
    q10 = st.selectbox('Technical Communication :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q11 = st.selectbox('AI ML :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q12 = st.selectbox('Software Engineering :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q13 = st.selectbox('Business Analysis :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q14 = st.selectbox('Communication skills :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q15 = st.selectbox('Data Science :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q16 = st.selectbox('Troubleshooting skills :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
    q17 = st.selectbox('Graphics Designing :  ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
st.text("")
st.text("")
st.text("")
st.text("")

b=st.button("Discover Yourself")

def mapping(q):
    if(q== 'Not Interested') :
        value = 1
        return value
    elif (q=="Poor"):
        value = 2
        return value

    elif (q=="Beginner"):
        value = 3
        return value

    elif (q=="Average"):
        value = 5
        return value

    elif (q=="Intermediate"):
        value = 6
        return value

    elif (q=="Excellent"):
        value = 7
        return value

    elif (q=="Professional"):
        value = 9
        return value

     



if b : 
#     if q1=='' or q2=='' or q3 == '' or q4=='' or q5=='' or q6 == '' or q7=='' or q8=='' or q9 == '' or q10=='' or q11=='' or q12 == '' or q13=='' or q14=='' or q15== '' or q16=='' or q17=='' :
#         st.error('please choose all the detials from dropdown. Do not leave them blank !!')

    # else:
        data1 = {
            'Database Fundamentals': [mapping(q1)],
            'Computer Architecture': [mapping(q2)],
            'Distributed Computing Systems': [mapping(q3)],
            'Cyber Security': [mapping(q4)],
            'Networking': [mapping(q5)],
            'Software Development': [mapping(q6)],
            'Programming Skills': [mapping(q7)],
            'Project Management': [mapping(q8)],
            'Computer Forensics Fundamentals': [mapping(q9)],
            'Technical Communication': [mapping(q10)],
            'AI ML': [mapping(q11)],
            'Software Engineering': [mapping(q12)],
            'Business Analysis': [mapping(q13)],
            'Communication skillsl': [mapping(q14)],
            'Data Science': [mapping(q15)],
            'Troubleshooting skills': [mapping(q16)],
            'Graphics Designing': [mapping(q17)]
            }
        df = pd.DataFrame(data1)
        arr=df.iloc[0:1].to_numpy()
        prediction = model_1.predict(arr)

        st.write(prediction)




