import streamlit as st
import app2
import app1
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="UNIT OPERATIONS ARE COOL", layout="wide")



def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

    


st.sidebar.title("Navigation",)
page = st.sidebar.selectbox("Choose a page", ["Home", "Fick's Second Law", "Fick's Second Law Reaction"])


if page == "Home":
    tailwind_cdn = """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
        <style>
            /* Center the table header and cell content */
            .css-1q8dd3e.e1ewe7hr3 th, .css-1q8dd3e.e1ewe7hr3 td {
                text-align: center !important;
            }
        </style>
    """
    st.markdown(tailwind_cdn, unsafe_allow_html=True)
    
    

    st.markdown("""
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:-mb-12">          
    <h1 class="text-3xl  text-center font-extrabold mt-10 md:text-5xl
                cursor-pointer md:text-7xl md:font-extrabold
                mb-10 hover:text-red-400 duration-1000
                ">
                 UNIT OPERATIONS ARE 
                <span class="bg-red-100 text-red-600 md:text-6xl mt-2 text-3xl font-extrabold me-2 px-2.5 py-0.5 rounded dark:bg-red-400 dark:text-red-800 ms-2
                hover:scale-125">
                    COOL!
                </span>
    </h1>
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:-mt-7">
    """, unsafe_allow_html=True)

    
    url1 = get_url("https://lottie.host/b1031118-99fc-47da-8103-0d692d09c1cd/6Myzvt3heg.json")

    col1 , col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        <h1 class="text-center text-md  font-extrabold cursor-pointer capitalize hover:text-red-400 duration-1000 md:text-5xl md:mt-20
                ">
        Welcome to our project for chemical engineering students! This tool lets you explore and visualize key unit operations.
        </h1>

        <h1 class="text-center text-md  font-extrabold cursor-pointer capitalize hover:text-red-400 duration-1000 md:text-5xl 
                ">
        With engaging simulations, you can deepen your understanding of essential topics such as mass transfer and thermodynamics, providing a hands-on way to apply your knowledge.
        </h1>


    
    """, unsafe_allow_html=True)
    with col2:
        st_lottie(url1, width=500, height=500)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
elif page == "Fick's Second Law":
    app1.display1()

elif page == "Chemical Kinetics and Fick's Second Law with Reaction":
    app2.display2()
