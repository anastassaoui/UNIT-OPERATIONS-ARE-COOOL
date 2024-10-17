import requests
import time
import os
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from scipy.integrate import odeint
from streamlit_lottie import st_lottie
from langchain_groq import ChatGroq
#from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
#from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Groq API key not found. Make sure it's defined in the .env file.")

llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)





def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

url1 = get_url("https://lottie.host/01168c02-1c9e-493e-85f2-343c86c43950/fkBauqcPOH.json")
url2 = get_url("https://lottie.host/c8ce4ada-d2f8-42f8-ab21-689abf4e9aae/3yeact3Hyb.json")
url3 = get_url("https://lottie.host/ec9a9ff6-561d-40c4-9d73-1d10cadb1773/IsBsAaSi64.json")
url4 = get_url("https://lottie.host/d4cbdfc3-631d-4868-a579-414c0f7c15ba/aTaSBPnHZE.json")
url5 = get_url("https://lottie.host/ba08f5b8-8d62-4c39-9cd9-80b3b7c2ed13/EYPiFLUScU.json")








def display1():
    
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

    col1,col2,col3 = st.columns([1,3,1])
    with col1:
        st_lottie(url1, width=300, height=300)
    with col2:
        st.markdown("""
        
        <h1 class="text-3xl  text-center font-extrabold mt-10 md:text-7xl
                    cursor-pointer md:text-7xl md:font-extrabold
                    mb-10 hover:text-red-400 duration-1000 md:mt-20
                    ">
                     Chemical 
                    <span class="bg-red-100 text-red-600 md:text-6xl mt-2 text-3xl font-extrabold me-2 px-2.5 py-0.5 rounded dark:bg-red-400 dark:text-red-800 ms-2
                    hover:scale-125">
                        Kinetics!
                    </span>
        </h1>


        """, unsafe_allow_html=True)
    with col3:
        st_lottie(url1, width=300, height=300)
    
    

    st.markdown("""

        <h4 class="text-xl font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer hover:underline md:-mb-12 md:mt-20 md:text-4xl">
            Chemical Kinetics Deals With The Speed Or Rate At Which Chemical Reactions Occur:
        </h4>
        <p class="mb-3 text-lg  md:text-xl text-white md:mt-20 cursor-pointer">
            The rate of a chemical reaction depends on reactant concentration and the rate constant. The reaction rate increases with higher concentrations and is influenced by temperature, catalysts, and activation energy. The Arrhenius equation links temperature to the rate constant, showing how molecular collisions affect reaction speed, making it essential to optimize conditions in chemical processes.
        </p>
        """, unsafe_allow_html=True)
    col1,col2 = st.columns([2,1])
    with col1:
        st.latex(r"""
            \textbf{First-Order Reactions}
            """)

        st.latex(r"""
            \text{Rate} = -\frac{d[A]}{dt} = k[A]
            """)
        st.latex(r"""
            \text{Rate of a first-order reaction is directly proportional to the concentration.}
            """)
        st.latex(r"""
            \text{Differential equation:}
            """)
        st.latex(r"""
            \frac{d[A]}{dt} = -k[A]
            """)
        st.latex(r"""
            \text{Solution:}
            """)
        st.latex(r"""
            [A](t) = [A]_0 e^{-kt}
            """)
    with col2:
        st_lottie(url2, width=400, height=400)
        
        
        
        
    col1,col2 = st.columns([1,2])
    with col1:
        st_lottie(url3, width=350, height=400)
    
    
    with col2:
        st.latex(r"""
            \textbf{Second-Order Reactions}
            """)
        st.latex(r"""
            \text{Rate} = -\frac{d[A]}{dt} = k[A]^2
            """)
        st.latex(r"""
            \text{The rate is proportional to the square of the concentration of the reactant.}
            """)
        st.latex(r"""
            \text{Differential equation:}
            """)
        st.latex(r"""
            \frac{d[A]}{dt} = -k[A]^2
            """)
        st.latex(r"""
            \text{Solution:}
            """)
        st.latex(r"""
            [A](t) = \frac{[A]_0}{1 + k[A]_0 t}
            """)
    col1,col2 = st.columns([2,1])
    
    with col1:
        st.latex(r"""
            \textbf{Third-Order Reactions}
            """)
        st.latex(r"""
            \text{Rate} = -\frac{d[A]}{dt} = k[A]^3
            """)
        st.latex(r"""
            \text{The rate is proportional to the cube of the concentration of the reactant.}
            """)
        st.latex(r"""
            \text{Differential equation:}
            """)
        st.latex(r"""
            \frac{d[A]}{dt} = -k[A]^3
            """)
        st.latex(r"""
            \text{Solution:}
            """)
        st.latex(r"""
            [A](t) = \frac{[A]_0}{(1 + 2k[A]_0^2 t)^{1/2}}
            """)
    with col2:
        st_lottie(url4, width=400, height=450)

    ##😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️
    ##😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️
    ##😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️
    ##😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️😊😘😂😊💕😁😁👌💕😁❤️👌😁🤦‍♂️😎😉🤷‍♂️

    def first_order(C, t, k):
        return -k * C

    def second_order(C, t, k):
        return -k * C**2

    def third_order(C, t, k):
        return -k * C**3

    st.sidebar.title("Parameters")

    reaction_order = st.sidebar.selectbox(
        "Select Reaction Order",
        ("First Order", "Second Order", "Third Order"),
        key='reaction_order_extended'
    )

    k = st.sidebar.slider("Rate Constant (k)", min_value=0.0, max_value=20.0, value=1.0)
    C0 = st.sidebar.slider("Initial Concentration (C₀)", min_value=0.001, max_value=50.0, value=1.0)
    time_max = st.sidebar.slider("Maximum Time", min_value=1, max_value=100, value=50)

    t = np.linspace(0, time_max, 80)

    #progress bar
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # Calculate concentration based on selected reaction order
    if reaction_order == "First Order":
        C = odeint(first_order, C0, t, args=(k,))
    elif reaction_order == "Second Order":
        C = odeint(second_order, C0, t, args=(k,))
    elif reaction_order == "Third Order":
        C = odeint(third_order, C0, t, args=(k,))

    # Update progress bar
    for i in range(1, 101):
        time.sleep(0.01)  #progress delay
        progress_bar.progress(i)
        status_text.text(f"{i}% Complete")

    progress_bar.empty()



    col1, col2 = st.columns([1, 1])
    with col1:
        # Plot the data
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=C[:, 0], mode='lines', name='Concentration'))

        fig.update_layout(
            title='Concentration vs Time',
            xaxis_title='Time',
            yaxis_title='Concentration',
            template='plotly_dark'
        )

        st.plotly_chart(fig)

    C0_doubled = 2 * C0
    c0_tripplled =3 * C0
    c0_quad =4 * C0
    c0_cinq =5 * C0    
    

    if reaction_order == "First Order":
        C_doubled = odeint(first_order, C0_doubled, t, args=(k,))
    elif reaction_order == "Second Order":
        C_doubled = odeint(second_order, C0_doubled, t, args=(k,))
    elif reaction_order == "Third Order":
        C_doubled = odeint(third_order, C0_doubled, t, args=(k,))
        
    if reaction_order == "First Order":
        C_trip = odeint(first_order, c0_tripplled, t, args=(k,))
    elif reaction_order == "Second Order":
        C_trip = odeint(second_order, c0_tripplled, t, args=(k,))
    elif reaction_order == "Third Order":
        C_trip = odeint(third_order, c0_tripplled, t, args=(k,))
        
    if reaction_order == "First Order":
        C_quad = odeint(first_order, c0_quad, t, args=(k,))
    elif reaction_order == "Second Order":
        C_quad = odeint(second_order, c0_quad, t, args=(k,))
    elif reaction_order == "Third Order":
        C_quad = odeint(third_order, c0_quad, t, args=(k,))
        
    if reaction_order == "First Order":
        C_quad = odeint(first_order, c0_quad, t, args=(k,))
    elif reaction_order == "Second Order":
        C_quad = odeint(second_order, c0_quad, t, args=(k,))
    elif reaction_order == "Third Order":
        C_quad = odeint(third_order, c0_quad, t, args=(k,))

    if reaction_order == "First Order":
        C_cinq = odeint(first_order, c0_cinq, t, args=(k,))
    elif reaction_order == "Second Order":
        C_cinq = odeint(second_order, c0_cinq, t, args=(k,))
    elif reaction_order == "Third Order":
        C_cinq = odeint(third_order, c0_cinq, t, args=(k,))
        
        
        
            
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=t, y=C[:, 0], mode='lines', name=f'C₀ = {C0}'))
        fig2.add_trace(go.Scatter(x=t, y=C_doubled[:, 0], mode='lines', name=f'C₀ = {C0_doubled}'))
        fig2.add_trace(go.Scatter(x=t, y=C_trip[:, 0], mode='lines', name=f'C₀ = {c0_tripplled}'))
        fig2.add_trace(go.Scatter(x=t, y=C_quad[:, 0], mode='lines', name=f'C₀ = {c0_quad}'))
        fig2.add_trace(go.Scatter(x=t, y=C_cinq[:, 0], mode='lines', name=f'C₀ = {c0_cinq}'))


        fig2.update_layout(
            title='Effect of Doubling Initial Concentration',
            xaxis_title='Time',
            yaxis_title='Concentration',
            template='plotly_dark'
        )

        st.plotly_chart(fig2)

    rate_of_change = -k * C[:, 0] if reaction_order == "First Order" else -k * C[:, 0]**(2 if reaction_order == "Second Order" else 3)
    half_life = np.log(2) / k if reaction_order == "First Order" else 1 / (k * C0) if reaction_order == "Second Order" else None

        




    # Create the DataFrame with added columns
    reaction_rate = k * C[:, 0] if reaction_order == "First Order" else k * C[:, 0]**(2 if reaction_order == "Second Order" else 3)
    relative_rate_of_change = rate_of_change / C0
    reaction_quotient = (C0 - C[:, 0]) / C[:, 0] #A -> B reaction
    log_concentration = np.log(C[:, 0])
    data = pd.DataFrame({
    'Time': t,
    'Concentration': C[:, 0],
    'Rate of Change': rate_of_change,
    'Normalized Concentration': C[:, 0] / C0,
    'Cumulative Change': np.cumsum(np.diff(C[:, 0], prepend=C0)),
    'Half-Life': half_life if half_life else 'N/A',
    'Relative Rate of Change': relative_rate_of_change,
    'Reaction Quotient (Q)': reaction_quotient,
    'Logarithm of Concentration': log_concentration
    })

    # Column selection with multiselect
    selected_columns = st.multiselect(
        "Select what to display:",
        options=data.columns.tolist(),
        default=data.columns.tolist()
    )

    # Display the selected columns in a dataframe
    st.write("### Concentration Data Over Time")
    st.dataframe(data[selected_columns], use_container_width=True)
           

        
        
    col1,col2,col3 = st.columns([2,1,2])
    with col1:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=t, y=rate_of_change, mode='lines', name='Rate of Change'))
        fig3.update_layout(
            title='Rate of Change of Concentration vs. Time',
            xaxis_title='Time',
            yaxis_title='Rate of Change',
            template='plotly_dark'
        )
        st.plotly_chart(fig3)

    with col3:
        fig6 = go.Figure()

        fig6.add_trace(go.Scatter(x=C[:, 0], y=rate_of_change, mode='lines', name='Phase Plot'))

        fig6.update_layout(
            title='Concentration vs Rate of Change',
            xaxis_title='Concentration',
            yaxis_title='Rate of Change',
            template='plotly_dark'
        )

        st.plotly_chart(fig6)

    with col2:
        st_lottie(url5, width=200, height=500)

    
    
    st.markdown("""
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:-mb-12">          
    <h1 class="text-3xl  text-center font-extrabold mt-10 md:text-5xl
                cursor-pointer md:text-7xl md:font-extrabold
                mb-10 hover:text-red-400 duration-1000
                ">
                CHECK OUT
                <span class="bg-red-100 text-red-600 md:text-6xl mt-2 text-3xl font-extrabold me-2 px-2.5 py-0.5 rounded dark:bg-red-400 dark:text-red-800 ms-2
                hover:scale-125">
                    DOCUMENTATION!
                </span>
    </h1>
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:-mt-7">
    """, unsafe_allow_html=True)    
    
    # Google Drive embeddable URL for the PDF
    pdf_url = "https://drive.google.com/file/d/1InJd_GbkjPPZWJCaaqv3VvAmhNAqC_0G/preview"
        # Embed the Google Drive PDF in an iframe
    st.markdown(f'<iframe src="{pdf_url}" width="1000" height="1000"></iframe>', unsafe_allow_html=True)


    st.markdown("""
  
    <h1 class="text-3xl  text-center font-extrabold mt-10 md:text-4xl
                cursor-pointer md:text-7xl md:font-extrabold
                mb-10 hover:text-red-400 duration-1000 md:mt-20
                ">
                Ask the AI a question about the 
                <span class="bg-red-100 text-red-600 md:text-6xl mt-2 text-3xl font-extrabold me-2 px-2.5  rounded dark:bg-red-400 dark:text-red-800 ms-2 
                hover:scale-125">
                    chemical kinetics data
                </span>
    </h1>
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:-mt-7">
    """, unsafe_allow_html=True)    
    
    


    user_question = st.text_input("")

    if user_question:
        # Convert DataFrame to a string summary for the AI to process
        data_summary = data.iloc[:80, :].to_csv(index=False)

        # Generate the context for the question including the data summary
        context = f"""
        The following chemical kinetics data has been calculated:
        {data_summary}
        Analyze this data and answer the user's question.
        """

        #system message
        system_message = SystemMessage(content=context)

        #human message
        user_message = HumanMessage(content=user_question)

        result = llm.invoke([system_message, user_message])

        # Parse
        parser = StrOutputParser()
        parsed_result = parser.invoke(result)

        # Display
        st.code(parsed_result, language='python')  # Change the language as needed


    
if __name__ == "__main__":
    display1()