import streamlit as st
import app2
import app1
import json
import requests
from streamlit_lottie import st_lottie
import os
st.set_page_config(page_title="Absence Management Dashboard", layout="wide")

# Function to load a Lottie animation from a file
def load_lottie_file(filepath):
    absolute_path = os.path.abspath(filepath)
    
    if not os.path.exists(filepath):
        st.error(f"File not found: {filepath}")
        return None

    with open(filepath, 'r') as f:
        return json.load(f)


# Function to load a Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Streamlit navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Fick's Second Law", "Chemical Kinetics and Fick's Second Law with Reaction"])

# Display Lottie animation at the top of the page
lottie_animation = load_lottie_file('lottie_files/animation.json')
st_lottie(lottie_animation, height=200, key="animation")

# Conditional rendering based on the selected page
if page == "Fick's Second Law":
    app1.display1()

elif page == "Chemical Kinetics and Fick's Second Law with Reaction":
    app2.display2()
