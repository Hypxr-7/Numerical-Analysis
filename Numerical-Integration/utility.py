def trap_eq(n, a, b, f):
    """
    Approximates the definite integral of a function using the trapezoidal rule.
    Parameters:
    n (int): The number of subintervals.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    f (function): The function to integrate. It must be a function of a single variable.
    Returns:
    float: The approximate value of the definite integral of f from a to b.
    """
    h = (b - a) / n
    x = a
    total = f(x)
    for _ in range(1, n):
        x += h
        total += 2 * f(x)

    total += f(b)

    return (b - a) * total / (2 * n)