import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import sklearn
import pandas as pd
import numpy as np 
import pickle
import webbrowser
@st.cache_resource


def load_model():
    with open('knn_model.pkl', 'rb') as file:
        loaded_ml_model = pickle.load(file)
    return loaded_ml_model

# st.set_page_config(initial_sidebar_state="collapsed")
st.header("MapYourFuture")


# st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
# unsafe_allow_html=True,
# )
#st.set_page_config(layout="wide", page_title='Map Your Future')

#####################################################
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#######################################################


#######################################################

# nav bar

# selected = option_menu(
# menu_title = None,
#  options = ["Home","Discover","Contact"],
#  default_index=0,
# orientation="horizontal",
# )
#######################################################

with st.sidebar:
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight:bold;
    }
                [data-testid="css-6qob1r eczjsme3"]{{
background-image: url("https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80");
background-position: center;}}
                
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Clarity preceeds Success.</p>', unsafe_allow_html=True)
    st.write("An ML based career advisory platform for CS students.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("Algorithm used: K-Nearest Neighbor ")
    st.subheader("Accuracy of the model : 96.732 % ")



model_1 = load_model() 

# col1, ecol, col2 = st.columns([1.5, 0.2, 1.5])

# with col1:
q1 = st.selectbox('**How good are you in DBMS and SQL?** ',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q2 = st.selectbox('**Rate your awareness of different components of computer architecture.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q3 = st.selectbox('**Are you strong at Database Fundamentals and topics of Operating systems?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q4 = st.selectbox('**Rate your knowledge on firewall and security risk management.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q5 = st.selectbox('**Rate your knowledge on various networking protocols.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q6 = st.selectbox('**How good are you in maintaining interoperability among multiple technologies?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q7 = st.selectbox('**Rate yourself on problem solving and analytical thinking abilities.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q8 = st.selectbox('**Rate your Leadership qualities.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q9 = st.selectbox('**Rate your Understanding on Biometrics and Crime Investigation.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
# with col2 :
q10 = st.selectbox('**How Frequent do you refer to technical aspects in a discussion?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q11 = st.selectbox('**Rate your Knowledge on machine learning models and Artificial intelligence.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q12 = st.selectbox('**How good are you at multitasking and giving attention to detail?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q13 = st.selectbox('**Rate your knowledge on statistics and data visualization tools.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q14 = st.selectbox('**Rate your communication skills.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q15 = st.selectbox('**How good are you at programming and mathematics?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q16 = st.selectbox('**Rate your planning and testing abilities.**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))
q17 = st.selectbox('**How good are you at designing User Interface and crafting branding techniques?**',('','Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate', 'Excellent', 'Professional'))

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
    if q1=='' or q2=='' or q3 == '' or q4=='' or q5=='' or q6 == '' or q7=='' or q8=='' or q9 == '' or q10=='' or q11=='' or q12 == '' or q13=='' or q14=='' or q15== '' or q16=='' or q17=='' :
        st.error('please choose all the detials from dropdown. Do not leave them blank !!')

    else:
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
        st.write()
        st.write("You would become a good:")
        # import streamlit as st
        # from streamlit.components.v1 import html
        
        st.button(prediction[0])
        # def open_page(url):
        #     open_script= """
        #         <script type="text/javascript">
        #             window.open('%s', '_blank').focus();
        #         </script>
        #     """ % (url)
        #     html(open_script)

        # st.button(prediction[0], on_click=open_page, args=('https://roadmap.sh/ux-design',))







