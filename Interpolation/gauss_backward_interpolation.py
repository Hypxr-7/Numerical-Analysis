from utility import construct_table, fact

def gauss_backward_interpolation(x, y, int_x):
    fd = construct_table(y)

    start = len(y)/2 if len(y)%2 == 0 else len(y)//2
    start = int(start)

    val = fd[0][start]
    u = (int_x - x[start]) / (x[1] - x[0])
    start -= 1
    for i in range(1, len(y)):
        uu = calc_u(u, i)
        val += fd[i][start] * calc_u(u, i) / fact(i)
        if i % 2 == 0:
            start -= 1

    return val


def calc_u(u, n):
    temp = u
    for i in range(1, n):
        if i % 2 == 0:
            temp *= (u - i+1)
        else:
            temp *= (u + i)
    return temp


if __name__ == '__main__':
    int_x = 5
    x = [ 2,  4,  6,  8]
    y = [10, 18, 26, 40]

    print(f'Value at {int_x} = {gauss_backward_interpolation(x, y, int_x):.3f}')
