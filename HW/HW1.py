import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# EXERCISE 1

x = sp.symbols('x')

# Define functions using SymPy's Piecewise for conditional logic
def f1(x):
    return sp.Piecewise((0, x < -sp.pi/2), (0, x > sp.pi/2), (1/2 * sp.cos(x), True))

def f2(x):
    return 1/(1 + sp.exp(-x))

def f3(x):
    return sp.Piecewise((0, x < 0), (0, x > 1), ((x**3)/3, True))

def f4(x):
    return sp.Piecewise((0, x <= 0), (1/x, True))

def f5(x):
    return sp.Piecewise((0, x < 0), (2**(-x), True))

# Test for Axiom 1: Check if f(x) >= 0 for all x in the range
def testAxiom1(f):
    # The reason this can be done with linspace is because the functions are continuous
    for val in np.linspace(-10, 10, 100):
        if f(val).evalf() < 0:
            return False
    return True

# Test for Axiom 2: Check if the integral of f(x) from -inf to inf equals 1
def testAxiom2(f, is_natural_numbers=False, include_zero=False):
    if is_natural_numbers:
        start = 0 if include_zero else 1
        sum_result = sp.Sum(f(x), (x, start, sp.oo))
        return sp.simplify(sum_result) == 1
    else:
        integral = sp.integrate(f(x), (x, -sp.oo, sp.oo))
        return sp.simplify(integral) == 1


def exercise1 () :
    print("Exercise 1\n")
    # Test functions
    print("f1 ax1:", testAxiom1(f1), " ax2: ", testAxiom2(f1))
    print("f2 ax1:", testAxiom1(f2), " ax2: ", testAxiom2(f2))
    print("f3 ax1:", testAxiom1(f3), " ax2: ", testAxiom2(f3))
    print("f4 ax1:", testAxiom1(f4), " ax2: ", testAxiom2(f4, is_natural_numbers=True))
    print("f5 ax1:", testAxiom1(f5), " ax2: ", testAxiom2(f5, is_natural_numbers=True, include_zero=True))
    exercise1_graphs()

def exercise1_graphs () :
    # Print graphs
    x_vals = np.linspace(-3, 10, 100)
    f1_vals = [f1(val).evalf() for val in x_vals]
    f2_vals = [f2(val).evalf() for val in x_vals]
    f3_vals = [f3(val).evalf() for val in x_vals]
    f4_vals = [f4(val).evalf() for val in x_vals]
    f5_vals = [f5(val).evalf() for val in x_vals]
    plt.plot(x_vals, f1_vals, label='f1')
    plt.plot(x_vals, f2_vals, label='f2')
    plt.plot(x_vals, f3_vals, label='f3')
    plt.plot(x_vals, f4_vals, label='f4')
    plt.plot(x_vals, f5_vals, label='f5')
    plt.legend()
    plt.show()

# EXERCISE 2

t = sp.symbols('t')

def f (t):
    # t measured in years
    return sp.Piecewise((0, t < 0), (0.1*sp.exp(-0.1*t), True))

def exercise2 () :
    print("\n\nExercise 2\n")
    
    # We can see that the function is valid for both axioms and is therefore a valid probability density function
    # print("f1 ax1:", testAxiom1(f), " ax2: ", testAxiom2(f))

    # Mean lifetime
    # We know that mean = E(t) = integral(t*f(t)) from 0 to inf
    mean = sp.integrate(t*f(t), (t, 0, sp.oo))
    print("Mean lifetime: ", round(mean), " years")

    # Standard deviation
    # Variance = E[ (Y - E[Y])^2] = E[Y^2] - E[Y]^2
    # Standard deviation = sqrt(variance)
    variance = sp.integrate((t**2)*f(t), (t, 0, sp.oo)) - mean**2
    std_dev = sp.sqrt(variance)
    print("Standard deviation: ", round(std_dev), " years")

    # Probability of a system failing within  10 years
    prob = sp.integrate(f(t), (t, 10, sp.oo))
    print("Probability of failing within 10 years: ", round(1-prob, 3)*100, "%")

    # The median lifetime of the system
    # Median is the value of t such that P(t <= T) = 0.5
    # We can solve this by integrating f(t) from 0 to T and setting it equal to 0.5
    T = sp.symbols('T')
    median = sp.solve((sp.integrate(f(t), (t, 0, T)) - 0.5), T)
    print("Median lifetime: ", round(median[0], 2), " years")

    # The probability that at least one out of 5 systems will fail within 3 years
    # We can use the complement of the probability that all 5 systems will not fail within 3 years
    p_system_not_fail = 1 - sp.integrate(f(t), (t, 0, 3))
    p_none_of_system_fail = p_system_not_fail**5
    print("Probability of at least one system failing within 3 years: ", round(p_none_of_system_fail, 3)*100, "%")

    # The probability that all 5 systems will fail within 15 years
    p_system_fail = sp.integrate(f(t), (t, 0, 15))
    p_all_systems_fail = p_system_fail**5
    print("Probability of all 5 systems failing within 15 years: ", round(p_all_systems_fail, 3)*100, "%")
    

# Run the exercises

exercise1()
exercise2()
# Exercise 3 done by hand