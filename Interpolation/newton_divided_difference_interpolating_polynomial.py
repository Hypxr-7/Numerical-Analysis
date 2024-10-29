"""
Modify the following:
dp: contains the data points
x: the value to interpolate
"""

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

    for order in range(1, n):
        x_term *= (x - dp['x'][order-1])
        y_int_2 = y_int + fdd[order-1][0] * x_term
        ea.append(abs(y_int_2 - y_int))

        print(f"{order:<10} {y_int:<10.6f} {ea[order-1]:<10.6f}")

        y_int = y_int_2

    print(f"{n:<10} {y_int:<10.6f}")



if __name__ == '__main__':
    dp = {
        'x': [5, 7, 11, 13, 17],
        'f': [150, 392, 1452, 2366, 5202],
    }
    interpolate(dp, 9)
