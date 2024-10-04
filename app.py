import streamlit as st
# Title of the Streamlit app
st.title('Solution to the Differential Equation for Diffusion with Reaction BY TASSAOUI Anas')

# Author and date
st.write('Author: TASSAOUI Anas')
st.write('Date: Today\'s date')

# Display Table of Contents
st.markdown("""
**Table of Contents:**
1. First-Order Reaction
    - Differential Equation
    - Simplified Equation and Boundary Conditions
    - Solution of the Differential Equation
2. Second-Order Reaction
    - Formulation of the Problem
    - Solution Approach
    - Characteristic Equation
    - General Solution
    - Applying Boundary Conditions
    - Solving the Coefficients
3. Third-Order Reaction
    - Formulation of the Problem
    - Solution Approach
    - Attempted Analytical Solution
    - Boundary Conditions
    - Solving the Coefficients
""")

# First-Order Reaction
st.header('Chapter 1: First-Order Reaction')

# Differential Equation
st.subheader('Differential Equation')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - r_a = 0')
st.write('In this equation:')
st.write('''
- \( D_A \) is the diffusion coefficient of species \( A \),
- \( C_A \) is the concentration of species \( A \) as a function of position \( x \),
- \( r_a \) is the reaction rate term which, in this case, is assumed to be first-order, meaning it depends on \( C_A \) linearly. 
''')

st.write('For a first-order reaction, \( r_a \) can be expressed as \( k C_A \), where \( k \) is the rate constant. Therefore, the equation becomes:')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - k C_A = 0')

# Simplified Equation and Boundary Conditions
st.subheader('Simplified Equation and Boundary Conditions')
st.write('The simplified differential equation is:')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - k C_A = 0')
st.write('The boundary conditions are:')
st.latex(r'C_A(0) = C_A^i \quad \text{and} \quad C_A(\delta) = C_A^L')
st.write('''
- \( C_A(0) = C_A^i \): the concentration at \( x = 0 \) is \( C_A^i \),
- \( C_A(\delta) = C_A^L \): the concentration at \( x = \delta \) is \( C_A^L \), where \( \delta \) is the thickness or length of the diffusion region.
''')

# Solution of the Differential Equation
st.subheader('Solution of the Differential Equation')
st.write('We start by proposing a general solution of the form:')
st.latex(r'C_A(x) = e^{mx}')
st.write('Substituting this proposed solution into the differential equation:')
st.latex(r'D_A m^2 e^{mx} - k e^{mx} = 0')
st.write('We can factor out the exponential term:')
st.latex(r'e^{mx} (D_A m^2 - k) = 0')

st.write('Since \( e^{mx} \neq 0 \), the equation simplifies to:')
st.latex(r'D_A m^2 - k = 0')
st.write('Solving for \( m \):')
st.latex(r'm^2 = \frac{k}{D_A} \quad \Rightarrow \quad m = \pm \sqrt{\frac{k}{D_A}}')

st.write('Thus, the general solution to the differential equation is:')
st.latex(r'C_A(x) = A e^{\sqrt{\frac{k}{D_A}} x} + B e^{-\sqrt{\frac{k}{D_A}} x}')

# Applying the Boundary Conditions
st.subheader('Applying the Boundary Conditions')
st.write('Now, we apply the boundary conditions to solve for the constants \( A \) and \( B \).')

st.write('1. At \( x = 0 \), we know:')
st.latex(r'C_A(0) = A + B = C_A^i')

st.write('2. At \( x = \delta \), we know:')
st.latex(r'C_A(\delta) = A e^{\sqrt{\frac{k}{D_A}} \delta} + B e^{-\sqrt{\frac{k}{D_A}} \delta} = C_A^L')

st.write('We now have a system of two equations:')
st.latex(r'''
\begin{align*}
A + B &= C_A^i \\
A e^{\sqrt{\frac{k}{D_A}} \delta} + B e^{-\sqrt{\frac{k}{D_A}} \delta} &= C_A^L
\end{align*}
''')

# Solving for A and B
st.subheader('Solving for \( A \) and \( B \)')
st.write('Let’s solve for \( A \) and \( B \) step by step:')
st.write('From the first equation:')
st.latex(r'B = C_A^i - A')

st.write('Substitute \( B = C_A^i - A \) into the second equation:')
st.latex(r'''
A e^{\sqrt{\frac{k}{D_A}} \delta} + (C_A^i - A) e^{-\sqrt{\frac{k}{D_A}} \delta} = C_A^L
''')

st.write('Simplify:')
st.latex(r'''
A \left( e^{\sqrt{\frac{k}{D_A}} \delta} - e^{-\sqrt{\frac{k}{D_A}} \delta} \right) + C_A^i e^{-\sqrt{\frac{k}{D_A}} \delta} = C_A^L
''')

st.write('Using the identity \( e^a - e^{-a} = 2\sinh(a) \), we get:')
st.latex(r'''
A \cdot 2\sinh\left( \sqrt{\frac{k}{D_A}} \delta \right) + C_A^i e^{-\sqrt{\frac{k}{D_A}} \delta} = C_A^L
''')

st.write('Now solve for \( A \):')
st.latex(r'''
A = \frac{C_A^L - C_A^i e^{-\sqrt{\frac{k}{D_A}} \delta}}{2\sinh\left( \sqrt{\frac{k}{D_A}} \delta \right)}
''')

st.write('Finally, substitute this value of \( A \) back into the equation \( B = C_A^i - A \) to get \( B \).')

st.write('This completes the solution for the concentration profile \( C_A(x) \) in a first-order reaction.')

# Final solution expression
st.subheader('Final Solution for \( C_A(x) \)')
st.write('Thus, the concentration profile is given by:')
st.latex(r'''
C_A(x) = A e^{\sqrt{\frac{k}{D_A}} x} + B e^{-\sqrt{\frac{k}{D_A}} x}
''')


# Second-Order Reaction
st.header('Chapter 2: Second-Order Reaction')

# Formulation of the Problem
st.subheader('Formulation of the Problem')
st.write('Assume the reaction rate \( r_a \) for a second-order reaction is given by:')
st.latex(r'r_a = k_2 C_R C_A')
st.write('Where:')
st.write('''
- \( k_2 \) is the second-order rate constant,
- \( C_R \) is the concentration of reactant \( R \),
- \( C_A \) is the concentration of species \( A \).
''')

st.write('Since \( C_R \) is in excess and treated as a constant, we can simplify the reaction rate to a pseudo-first-order form:')
st.latex(r'r_a = k^{\prime} C_A \quad \text{where} \quad k^{\prime} = k_2 C_R')

st.write('Thus, the differential equation governing the system becomes:')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - k^{\prime} C_A = 0')
st.write('Where:')
st.write('''
- \( D_A \) is the diffusion coefficient of species \( A \),
- \( C_A \) is the concentration of species \( A \) as a function of position \( x \),
- \( k^{\prime} \) is the pseudo-first-order rate constant.
''')

# Solution Approach
st.subheader('Solution Approach')
st.write('To solve this second-order differential equation, we propose a general solution of the form:')
st.latex(r'C_A(x) = A e^{mx} + B e^{-mx}')
st.write('Substituting this proposed solution into the differential equation:')
st.latex(r'D_A m^2 e^{mx} + D_A m^2 e^{-mx} - k^{\prime} A e^{mx} - k^{\prime} B e^{-mx} = 0')

st.write('Factor out the exponential terms:')
st.latex(r'e^{mx} (D_A m^2 - k^{\prime}) + e^{-mx} (D_A m^2 - k^{\prime}) = 0')

st.write('For this equation to hold true for all \( x \), each term must independently equal zero. Therefore:')
st.latex(r'D_A m^2 - k^{\prime} = 0')

st.write('Solving for \( m \):')
st.latex(r'm^2 = \frac{k^{\prime}}{D_A} \quad \Rightarrow \quad m = \pm \sqrt{\frac{k^{\prime}}{D_A}}')

# General Solution
st.subheader('General Solution')
st.write('Thus, the general solution to the differential equation is:')
st.latex(r'C_A(x) = A e^{\sqrt{\frac{k^{\prime}}{D_A}} x} + B e^{-\sqrt{\frac{k^{\prime}}{D_A}} x}')

# Applying Boundary Conditions
st.subheader('Applying the Boundary Conditions')
st.write('Next, we apply the boundary conditions to solve for the constants \( A \) and \( B \).')

st.write('1. At \( x = 0 \), the concentration is:')
st.latex(r'C_A(0) = C_A^i = A + B')

st.write('2. At \( x = \delta \), the concentration is:')
st.latex(r'C_A(\delta) = A e^{\sqrt{\frac{k^{\prime}}{D_A}} \delta} + B e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} = C_A^L')

st.write('These two boundary conditions give us the following system of equations:')
st.latex(r'''
\begin{align*}
A + B &= C_A^i \\
A e^{\sqrt{\frac{k^{\prime}}{D_A}} \delta} + B e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} &= C_A^L
\end{align*}
''')

# Solving for A and B
st.subheader('Solving for \( A \) and \( B \)')
st.write('Let’s solve for \( A \) and \( B \) step by step.')

st.write('From the first equation:')
st.latex(r'B = C_A^i - A')

st.write('Substitute this into the second equation:')
st.latex(r'''
A e^{\sqrt{\frac{k^{\prime}}{D_A}} \delta} + (C_A^i - A) e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} = C_A^L
''')

st.write('Simplify the equation:')
st.latex(r'''
A \left( e^{\sqrt{\frac{k^{\prime}}{D_A}} \delta} - e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} \right) + C_A^i e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} = C_A^L
''')

st.write('Using the identity \( e^a - e^{-a} = 2\sinh(a) \), we get:')
st.latex(r'''
A \cdot 2\sinh\left( \sqrt{\frac{k^{\prime}}{D_A}} \delta \right) + C_A^i e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta} = C_A^L
''')

st.write('Now solve for \( A \):')
st.latex(r'''
A = \frac{C_A^L - C_A^i e^{-\sqrt{\frac{k^{\prime}}{D_A}} \delta}}{2\sinh\left( \sqrt{\frac{k^{\prime}}{D_A}} \delta \right)}
''')

st.write('Substitute \( A \) back into the equation \( B = C_A^i - A \) to get \( B \):')
st.latex(r'B = C_A^i - A')

# Final solution expression
st.subheader('Final Solution for \( C_A(x) \)')
st.write('Thus, the concentration profile is given by:')
st.latex(r'''
C_A(x) = A e^{\sqrt{\frac{k^{\prime}}{D_A}} x} + B e^{-\sqrt{\frac{k^{\prime}}{D_A}} x}
''')

# Third-Order Reaction
st.header('Chapter 3: Third-Order Reaction')

# Formulation of the Problem
st.subheader('Formulation of the Problem')
st.write('For a third-order reaction, the rate equation is:')
st.latex(r'r_a = k_3 C_A^2 C_R')
st.write('Assuming \( C_R \) is constant, we simplify to:')
st.latex(r'r_a = k^{\prime} C_A^2 \quad \text{where} \quad k^{\prime} = k_3 C_R')
st.write('The differential equation then becomes:')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - k^{\prime} C_A^2 = 0')

# Attempted Analytical Solution
st.subheader('Attempted Analytical Solution')
st.write('We attempt a solution of the form:')
st.latex(r'C_A(x) = \frac{1}{(A x + B)^2}')
st.write('Substituting into the differential equation yields:')
st.latex(r'D_A \frac{6A^2}{(A x + B)^4} - k^{\prime} \frac{1}{(A x + B)^4} = 0')
st.latex(r'6A^2 D_A - k^{\prime} = 0 \quad \Rightarrow \quad A^2 = \frac{k^{\prime}}{6D_A}')

# Boundary Conditions
st.subheader('Boundary Conditions')
st.write('We apply the boundary conditions:')
st.latex(r'C_A(0) = C_A^i = \frac{1}{B^2}')
st.latex(r'C_A(\delta) = C_A^L = \frac{1}{(A \delta + B)^2}')

# Solving the Coefficients
st.subheader('Solving the Coefficients')
st.write('From the boundary condition \( C_A^i = \frac{1}{B^2} \), we get:')
st.latex(r'B = \frac{1}{\sqrt{C_A^i}}')
st.write('Then, using \( C_A(\delta) = C_A^L \), we solve for \( A \).')

# Third-Order Reaction
st.header('Chapter 3: Third-Order Reaction')

# Formulation of the Problem
st.subheader('Formulation of the Problem')
st.write('For a third-order reaction, the reaction rate is proportional to the square of the concentration of species \( A \) and the concentration of species \( R \). Therefore, the rate equation is given by:')
st.latex(r'r_a = k_3 C_A^2 C_R')
st.write('Where:')
st.write('''
- \( k_3 \) is the third-order rate constant,
- \( C_A \) is the concentration of species \( A \),
- \( C_R \) is the concentration of species \( R \).
''')

st.write('Assuming \( C_R \) is in excess and treated as constant, we simplify the reaction rate to:')
st.latex(r'r_a = k^{\prime} C_A^2 \quad \text{where} \quad k^{\prime} = k_3 C_R')

st.write('The corresponding differential equation for the concentration profile is:')
st.latex(r'D_A \frac{d^2 C_A}{dx^2} - k^{\prime} C_A^2 = 0')
st.write('Where:')
st.write('''
- \( D_A \) is the diffusion coefficient of species \( A \),
- \( C_A \) is the concentration of species \( A \) as a function of position \( x \),
- \( k^{\prime} \) is the pseudo-third-order rate constant.
''')

# Attempted Analytical Solution
st.subheader('Attempted Analytical Solution')
st.write('We will attempt an analytical solution by proposing a trial solution of the form:')
st.latex(r'C_A(x) = \frac{1}{(A x + B)^2}')

st.write('This is a commonly used trial solution for nonlinear differential equations of this type. Let’s substitute this into the differential equation:')

st.latex(r'D_A \frac{d^2}{dx^2} \left( \frac{1}{(A x + B)^2} \right) - k^{\prime} \left( \frac{1}{(A x + B)^2} \right)^2 = 0')

st.write('First, compute the second derivative of \( C_A(x) = \frac{1}{(A x + B)^2} \):')
st.latex(r'\frac{d}{dx} \left( \frac{1}{(A x + B)^2} \right) = \frac{-2A}{(A x + B)^3}')
st.latex(r'\frac{d^2}{dx^2} \left( \frac{1}{(A x + B)^2} \right) = \frac{6A^2}{(A x + B)^4}')

st.write('Now substitute this into the differential equation:')
st.latex(r'D_A \frac{6A^2}{(A x + B)^4} - k^{\prime} \frac{1}{(A x + B)^4} = 0')

st.write('Factor out the common term \( \frac{1}{(A x + B)^4} \):')
st.latex(r'\frac{1}{(A x + B)^4} \left( 6A^2 D_A - k^{\prime} \right) = 0')

st.write('For this equation to hold true, the term in parentheses must equal zero:')
st.latex(r'6A^2 D_A - k^{\prime} = 0')

st.write('Solving for \( A^2 \):')
st.latex(r'A^2 = \frac{k^{\prime}}{6D_A}')
st.write('Thus, \( A \) can be expressed as:')
st.latex(r'A = \pm \sqrt{\frac{k^{\prime}}{6D_A}}')

# Boundary Conditions
st.subheader('Applying the Boundary Conditions')
st.write('Next, we apply the boundary conditions to determine the constants \( A \) and \( B \).')

st.write('1. At \( x = 0 \), the concentration is:')
st.latex(r'C_A(0) = C_A^i = \frac{1}{B^2}')

st.write('2. At \( x = \delta \), the concentration is:')
st.latex(r'C_A(\delta) = C_A^L = \frac{1}{(A \delta + B)^2}')

# Solving the Coefficients
st.subheader('Solving the Coefficients')
st.write('From the boundary condition at \( x = 0 \):')
st.latex(r'C_A^i = \frac{1}{B^2}')
st.write('Solving for \( B \):')
st.latex(r'B = \frac{1}{\sqrt{C_A^i}}')

st.write('Now substitute \( B \) into the boundary condition at \( x = \delta \):')
st.latex(r'C_A^L = \frac{1}{(A \delta + B)^2}')

st.write('Substitute the expression for \( B \):')
st.latex(r'C_A^L = \frac{1}{\left( A \delta + \frac{1}{\sqrt{C_A^i}} \right)^2}')

st.write('Now solve for \( A \) using this equation.')

# Final Solution
st.subheader('Final Solution for \( C_A(x) \)')
st.write('Thus, the concentration profile for the third-order reaction is given by:')
st.latex(r'''
C_A(x) = \frac{1}{(A x + B)^2}
''')
st.write('Where \( A \) and \( B \) are determined using the boundary conditions as shown above.')