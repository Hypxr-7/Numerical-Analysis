from utility import construct_table, fact

def newtons_backward_interpolation(x, y, value):
    n = len(x)
    diff_table = construct_table(y)
    
    u = (value - x[-1]) / (x[1] - x[0])
    result = diff_table[0][-1]

    for i in range(1, n):
        result += calc_u(u, i) * diff_table[i][-1] / fact(i)
    
    return result


def calc_u(u, i):
    temp = u
    for j in range(1, i):
        temp *= (u + j)
    return temp


if __name__ == '__main__':
    x = [100, 150, 200, 250, 300, 350, 400]
    y = [10.63, 13.03, 15.04, 16.81, 18.42, 19.90, 21.27]
    value = 410
    print("Interpolated value at", value, "is", newtons_backward_interpolation(x, y, value))