

def gauss_forward_interpolation(x, y, int_x):
    # Construct table
    fd = [y]
    for i in range(1, len(y)):
        temp = []
        for j in range(0, len(y)-i):
            temp.append(fd[i-1][j+1] - fd[i-1][j])
        fd.append(temp)


    start = len(y)/2 - 1 if len(y)%2 == 0 else len(y)//2
    start = int(start)

    val = fd[0][start]
    u = (int_x - x[start]) / (x[1] - x[0])
    for i in range(1, len(y)):
        val += fd[i][start] * calc_u(u, i) / fact(i)
        if i % 2 == 1:
            start -= 1

    return val


def calc_u(u, n):
    temp = u
    for i in range(1, n):
        if i % 2 == 1:
            temp *= (u - i)
        else:
            temp *= (u + i-1)
    return temp


def fact(num):
    if num == 0:
        return 1

    result = num
    while num != 1:
        result *= num-1
        num -= 1
    return result


if __name__ == '__main__':
    int_x = 5
    x = [ 2,  4,  6,  8]
    y = [10, 18, 26, 40]

    print(f'Value at {int_x} = {gauss_forward_interpolation(x, y, int_x):.3f}')