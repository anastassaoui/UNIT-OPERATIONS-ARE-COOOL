import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from scipy.integrate import odeint
from streamlit_lottie import st_lottie
import requests
import time



def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

url1 = get_url("https://lottie.host/01168c02-1c9e-493e-85f2-343c86c43950/fkBauqcPOH.json")
url2 = get_url("https://lottie.host/c8ce4ada-d2f8-42f8-ab21-689abf4e9aae/3yeact3Hyb.json")


def display1():
    
    ###################################tailwind stuff##############################################
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
    
    ##############################################################################################
    
    
    #############################################Title###########################################
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
    ########################################################################################
    
    

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
        
    st.latex(r"""
        \textbf{Second-Order Reactions}
        """)
    st.latex(r"""
        \text{Rate law:}
        """)
    st.latex(r"""
        \text{Rate} = -\frac{d[A]}{dt} = k[A]^2
        """)
    st.latex(r"""
        \text{In a second-order reaction, the rate is proportional to the square of the concentration of the reactant.}
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

    st.latex(r"""
        \textbf{Third-Order Reactions}
        """)
    st.latex(r"""
        \text{Rate law:}
        """)
    st.latex(r"""
        \text{Rate} = -\frac{d[A]}{dt} = k[A]^3
        """)
    st.latex(r"""
        \text{The rate of a third-order reaction is proportional to the cube of the concentration of the reactant.}
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
    C0 = st.sidebar.slider("Initial Concentration (C₀)", min_value=0.0, max_value=20.0, value=1.0)
    time_max = st.sidebar.slider("Maximum Time", min_value=1, max_value=100, value=50)

    t = np.linspace(0, time_max, 500)

    # Add progress bar and status text
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    # Calculate concentration based on selected reaction order
    if reaction_order == "First Order":
        C = odeint(first_order, C0, t, args=(k,))
    elif reaction_order == "Second Order":
        C = odeint(second_order, C0, t, args=(k,))
    elif reaction_order == "Third Order":
        C = odeint(third_order, C0, t, args=(k,))

    # Update progress bar to indicate completion
    for i in range(1, 101):
        time.sleep(0.01)  # Simulate progress delay
        progress_bar.progress(i)
        status_text.text(f"{i}% Complete")

    # Clear the progress bar after computation is done
    progress_bar.empty()



    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        # Plot the data
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=C[:, 0], mode='lines', name='Concentration'))

        fig.update_layout(
            title='Concentration vs. Time',
            xaxis_title='Time',
            yaxis_title='Concentration',
            template='plotly_dark'
        )

        st.plotly_chart(fig)

    # Calculate and compare different initial concentrations
    C0_doubled = 2 * C0

    if reaction_order == "First Order":
        C_doubled = odeint(first_order, C0_doubled, t, args=(k,))
    elif reaction_order == "Second Order":
        C_doubled = odeint(second_order, C0_doubled, t, args=(k,))
    elif reaction_order == "Third Order":
        C_doubled = odeint(third_order, C0_doubled, t, args=(k,))
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=t, y=C[:, 0], mode='lines', name=f'C₀ = {C0}'))
        fig2.add_trace(go.Scatter(x=t, y=C_doubled[:, 0], mode='lines', name=f'C₀ = {C0_doubled}'))

        fig2.update_layout(
            title='Effect of Doubling Initial Concentration',
            xaxis_title='Time',
            yaxis_title='Concentration',
            template='plotly_dark'
        )

        st.plotly_chart(fig2)

    rate_of_change = -k * C[:, 0] if reaction_order == "First Order" else -k * C[:, 0]**(2 if reaction_order == "Second Order" else 3)
    half_life = np.log(2) / k if reaction_order == "First Order" else 1 / (k * C0) if reaction_order == "Second Order" else None
    with col3:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=t, y=rate_of_change, mode='lines', name='Rate of Change'))

        fig3.update_layout(
            title='Rate of Change of Concentration vs. Time',
            xaxis_title='Time',
            yaxis_title='Rate of Change',
            template='plotly_dark'
        )

        st.plotly_chart(fig3)
        # Create a DataFrame to display the data
        


    col1, col2 = st.columns([2,2])  
    with col1:
        
        data = pd.DataFrame({
            'Time': t,
            'Concentration': C[:, 0],
            'Rate of Change': rate_of_change,
            'Half-Life (if applicable)': half_life if half_life else 'N/A'
        })
        st.write("### Concentration Data Over Time", data)

        
           
    with col2:
        
        rate_data = pd.DataFrame({
            'Time': t,
            'Rate of Change': rate_of_change
        })
        st.write("### Rate of Change", rate_data)
    
    
    
if __name__ == "__main__":
    display1()