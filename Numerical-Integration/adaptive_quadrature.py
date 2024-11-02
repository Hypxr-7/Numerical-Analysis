def quad_apt(f, a, b, tol=0.000001):
    """
    Perform adaptive quadrature to numerically integrate a function over an interval [a, b].
    Parameters:
    f (function): The function to integrate.
    a (float): The start of the interval.
    b (float): The end of the interval.
    tol (float, optional): The tolerance for the adaptive quadrature. Default is 0.000001.
    Returns:
    float: The estimated integral of the function over the interval [a, b].
    The function uses Simpson's rule and recursively refines the interval until the estimated error is within the specified tolerance.
    """

    def q_step(a, b, tol, fa, fc, fb):
        h1 = b - a
        h2 = h1 / 2
        c = (a + b) / 2
        fd = f((a + c) / 2)
        fe = f((c + b) / 2)
        I1 = h1 / 6 * (fa + 4 * fc + fb)  # Simpson’s 1/3 rule
        I2 = h2 / 6 * (fa + 4 * fd + 2 * fc + 4 * fe + fb)
        
        if abs(I2 - I1) <= tol:
            return I2 + (I2 - I1) / 15
        else:
            Ia = q_step(a, c, tol, fa, fd, fc)
            Ib = q_step(c, b, tol, fc, fe, fb)
            return Ia + Ib

    c = (a + b) / 2
    fa = f(a)
    fc = f(c)
    fb = f(b)
    return q_step(a, b, tol, fa, fc, fb)


if __name__ == '__main__':
    f = lambda x : 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
    a = 0
    b = 0.8
    print(quad_apt(f, a, b))