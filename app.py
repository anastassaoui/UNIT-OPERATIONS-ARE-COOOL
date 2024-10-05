import streamlit as st
import numpy as np
import plotly.graph_objs as go
from scipy.integrate import odeint





st.set_page_config(page_title="Absence Management Dashboard", layout="wide")


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



st.title("Chemical Kinetics and Fick's Second Law with Reaction")

st.markdown("""
### Fick's Second Law with Reaction Term

When considering a reaction, Fick's Second Law becomes:

""")
st.latex(r"""
\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - R(C)
""")
st.markdown("""
Where:
- \( D \) is the diffusion coefficient,
- \( R(C) \) is the reaction rate, which depends on the concentration \( C \).
""")

st.markdown("""
### Reaction Orders

**First-Order Reaction:**
""")
st.latex(r"""
R(C) = k C
""")
st.markdown("""
Thus:
""")
st.latex(r"""
\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - k C
""")

st.markdown("""
**Second-Order Reaction:**
""")
st.latex(r"""
R(C) = k C^2
""")
st.markdown("""
Thus:
""")
st.latex(r"""
\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - k C^2
""")

st.markdown("""
### The Hatta Number (Ha)

The Hatta Number characterizes the relative rates of reaction and diffusion:

""")
st.latex(r"""
\text{Ha} = \frac{k C_0 L}{D}
""")
st.markdown("""
- **\( k \)**: Reaction rate constant
- **\( C_0 \)**: Initial concentration
- **\( L \)**: Characteristic length
- **\( D \)**: Diffusion coefficient

- **Ha << 1**: Reaction is slow compared to diffusion.
- **Ha >> 1**: Reaction is fast compared to diffusion.
""")

def reaction_term(Ci, k, order):
    if order == 1:
        return k * Ci
    elif order == 2:
        return k * Ci**2
    else:
        return 0

st.sidebar.title("Parameters")

reaction_order = st.sidebar.selectbox(
    "Select Reaction Order",
    ("First Order", "Second Order"),
    key='reaction_order_initial'    
)

D = st.sidebar.slider("Diffusion Coefficient (D)", min_value=0.1, max_value=10.0, value=1.0)
k = st.sidebar.slider("Reaction Rate Constant (k)", min_value=0.0, max_value=10.0, value=1.0)
C0 = st.sidebar.slider("Initial Concentration (C₀)", min_value=0.1, max_value=10.0, value=1.0)
L = st.sidebar.slider("Length of the Domain (L)", min_value=1.0, max_value=10.0, value=1.0)
N = st.sidebar.slider("Number of Spatial Points (N)", min_value=10, max_value=500, value=100)
time_max = st.sidebar.slider("Maximum Time", min_value=1, max_value=100, value=10)

Ha = (k * C0 * L) / D
st.sidebar.markdown(f"**Hatta Number (Ha):** {Ha:.2f}")

# Spatial discretization
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Time discretization
dt = 0.9 * dx**2 / (2 * D)  # Stability condition
time_steps = int(time_max / dt)
t = np.linspace(0, time_max, time_steps)

# Initial concentration profile
C = np.zeros((time_steps, N))
C[0, :] = C0  # Initial condition

# Boundary conditions (Dirichlet conditions)
C[:, 0] = C0  # Left boundary
C[:, -1] = C0  # Right boundary

# Time-stepping loop
for n in range(0, time_steps - 1):
    for i in range(1, N - 1):
        # Diffusion term
        diffusion = D * (C[n, i+1] - 2 * C[n, i] + C[n, i-1]) / dx**2
        # Reaction term
        if reaction_order == "First Order":
            reaction = -reaction_term(C[n, i], k, 1)
        elif reaction_order == "Second Order":
            reaction = -reaction_term(C[n, i], k, 2)
        else:
            reaction = 0
        # Update concentration
        C[n+1, i] = C[n, i] + dt * (diffusion + reaction)

# Select times to plot
plot_times = [0, int(0.25 * time_steps), int(0.5 * time_steps), int(0.75 * time_steps), time_steps - 1]
labels = ['t = 0', 't = 0.25 t_max', 't = 0.5 t_max', 't = 0.75 t_max', 't = t_max']

fig3 = go.Figure()

for idx, pt in enumerate(plot_times):
    fig3.add_trace(go.Scatter(x=x, y=C[pt, :], mode='lines', name=labels[idx]))

fig3.update_layout(
    title='Concentration Profile over Distance at Different Times',
    xaxis_title='Distance (x)',
    yaxis_title='Concentration (C)',
    template='plotly_dark'
)

st.plotly_chart(fig3)



