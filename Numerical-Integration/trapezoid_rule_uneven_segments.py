def trapezoid_uneven(x, y, n):
    sum_trap = 0
    for i in range(1, n):
        sum_trap += (x[i]-x[i-1]) * (y[i]+y[i-1]) / 2
    return sum_trap

if __name__ == '__main__':
    x = [0, 0.12, 0.22, 0.32, 0.36, 0.4, 0.44, 0.54, 0.64, 0.7, 0.8]
    y = [0.2, 1.309729, 1.305241, 1.743393, 2.074903, 2.456, 2.842985, 3.507297, 3.181929, 2.363, 0.232]

    print(trapezoid_uneven(x, y, len(x)))