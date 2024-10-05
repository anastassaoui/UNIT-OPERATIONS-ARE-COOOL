import streamlit as st




import streamlit as st
import app2
import app1

# Streamlit navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Fick's Second Law", "Chemical Kinetics and Fick's Second Law with Reaction"])

if page == "Fick's Second Law":
    app1.display1()


elif page == "Chemical Kinetics and Fick's Second Law with Reaction":
    app2.display2()
