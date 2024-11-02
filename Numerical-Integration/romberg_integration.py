from utility import trap_eq


def romberg(a, b, f, max_it=100, tol=0.5):
    """
    Perform Romberg integration to approximate the integral of a function.

    Parameters:
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    f (function): The function to integrate.
    max_it (int, optional): The maximum number of iterations. Default is 100.
    tol (float, optional): The tolerance for stopping criterion. Default is 0.5.

    Returns:
    float: The approximated integral of the function.
    """
    I = [[0] * (max_it + 1) for _ in range(max_it + 1)]
    n = 1
    I[0][0] = trap_eq(n, a, b, f)
    iteration = 0

    while True:
        iteration += 1
        n = 2 ** iteration
        I[iteration][0] = trap_eq(n, a, b, f)
        
        for k in range(1, iteration + 1):
            j = iteration - k
            I[j][k] = (4 ** k * I[j + 1][k - 1] - I[j][k - 1]) / (4 ** k - 1)
        
        I0_iter = I[0][iteration]
        ea = abs((I0_iter - I[1][iteration - 1]) / I0_iter) * 100
        if iteration >= max_it or ea <= tol:
            break

    return I[0][iteration]



if __name__ == '__main__':
    f = lambda x : 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
    a = 0
    b = 0.8
    print(romberg(a, b, f))