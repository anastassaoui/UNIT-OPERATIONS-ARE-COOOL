import streamlit as st
import numpy as np
import plotly.graph_objs as go
from scipy.integrate import odeint

st.set_page_config(page_title="Absence Management Dashboard", layout="wide")

   
def display1():

    st.title("Chemical Kinetics and Fick's Second Law")
    st.markdown("""
    ### Fick's Second Law

    Fick's Second Law describes diffusion and is given by:

    """)
    st.latex(r"""
    \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}
    """)
    st.markdown("""
    Where:
    - \( C \) is the concentration,
    - \( t \) is time,
    - \( D \) is the diffusion coefficient,
    - \( x \) is the spatial coordinate.
    """)

    st.markdown("""
    ### Reaction Orders

    The rate of a chemical reaction can depend on the concentration of reactants in different ways, known as reaction orders.

    **First-Order Reactions:**

    Rate law:
    """)
    st.latex(r"""
    \text{Rate} = -\frac{d[A]}{dt} = k[A]
    """)

    st.markdown("""
    Differential equation:
    """)
    st.latex(r"""
    \frac{d[A]}{dt} = -k[A]
    """)

    st.markdown("""
    **Second-Order Reactions:**

    Rate law:
    """)
    st.latex(r"""
    \text{Rate} = -\frac{d[A]}{dt} = k[A]^2
    """)

    st.markdown("""
    Differential equation:
    """)
    st.latex(r"""
    \frac{d[A]}{dt} = -k[A]^2
    """)

    def first_order(C, t, k):
        return -k * C

    def second_order(C, t, k):
        return -k * C**2

    st.sidebar.title("Parameters")

    reaction_order = st.sidebar.selectbox(
        "Select Reaction Order",
        ("First Order", "Second Order"),
        key='reaction_order_extended'
    )

    k = st.sidebar.slider("Rate Constant (k)", min_value=0.0, max_value=20.0, value=1.0)
    C0 = st.sidebar.slider("Initial Concentration (C₀)", min_value=0.0, max_value=20.0, value=1.0)
    time_max = st.sidebar.slider("Maximum Time", min_value=1, max_value=100, value=50)

    t = np.linspace(0, time_max, 500)

    if reaction_order == "First Order":
        C = odeint(first_order, C0, t, args=(k,))
    elif reaction_order == "Second Order":
        C = odeint(second_order, C0, t, args=(k,))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=C[:, 0], mode='lines', name='Concentration'))

    fig.update_layout(
        title='Concentration vs. Time',
        xaxis_title='Time',
        yaxis_title='Concentration',
        template='plotly_dark'
    )

    st.plotly_chart(fig)

    st.markdown("### Effect of Doubling the Initial Concentration")

    C0_doubled = 2 * C0

    if reaction_order == "First Order":
        C_doubled = odeint(first_order, C0_doubled, t, args=(k,))
    elif reaction_order == "Second Order":
        C_doubled = odeint(second_order, C0_doubled, t, args=(k,))

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
