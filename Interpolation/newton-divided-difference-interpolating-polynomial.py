import matplotlib.pyplot as plt
import numpy as np

'''
Modify the following:
dp: contains the data points
x: the value to interpolate
offset: extra portion of the graph to print
'''

def interpolate(dp, x):
    n = len(dp['x'])

    # Initialize fdd with the first column of divided differences
    fdd = [[(dp['f'][i + 1] - dp['f'][i]) / (dp['x'][i + 1] - dp['x'][i]) for i in range(n - 1)]]


    # Compute the rest of the divided difference table
    for j in range(1, n-1):
        temp_column = []
        for i in range(n-j-1):
            numerator = fdd[j-1][i+1] - fdd[j-1][i]
            denominator = dp['x'][i+j+1] - dp['x'][i]
            temp_column.append(numerator / denominator)
        fdd.append(temp_column)
    
    # Compute interpolated value at x
    x_term = 1
    y_int = dp['f'][0]
    ea = []

    print(f"{'Order':<10} {'f(x)':<10} {'Error':<10}")

    coefficients = [dp['f'][0]]

    for order in range(1, n):
        x_term *= (x - dp['x'][order-1])
        y_int_2 = y_int + fdd[order-1][0] * x_term
        ea.append(abs(y_int_2 - y_int))

        print(f"{order:<10} {y_int:<10.6f} {ea[order-1]:<10.6f}")

        y_int = y_int_2
        coefficients.append(fdd[order-1][0])

    print(f"{n:<10} {y_int:<10.6f}")

    return coefficients

def evaluate_polynomial(coefficients, x_points, x_data):
    n = len(coefficients)
    y_points = []
    for x in x_points:
        y = coefficients[0]
        x_term = 1
        for i in range(1, n):
            x_term *= (x - x_data[i-1])
            y += coefficients[i] * x_term
        y_points.append(y)
    return y_points

def original_function(x):
    # Define the original function here
    return np.log(x)

if __name__ == '__main__':
    dp = {
        'x': [1, 4, 6, 5, 3, 1.5, 2.5, 3.5],
        'f': [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123, 0.4054641, 0.9162907, 1.2527630],
    }
    
    coefficients = interpolate(dp, 2)

    left_offset = 0.5
    right_offset = 2
    # Plot the polynomial
    x_points = np.linspace(min(dp['x']) - left_offset, max(dp['x']) + right_offset, 100)
    y_points = evaluate_polynomial(coefficients, x_points, dp['x'])

    y_original = original_function(x_points)

    plt.plot(dp['x'], dp['f'], 'ro', label='Data Points')
    plt.plot(x_points, y_points, 'b-', label='Interpolated Polynomial')
    plt.plot(x_points, y_original, 'g--', label='Original Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Newton Divided Difference Interpolation')
    plt.show()