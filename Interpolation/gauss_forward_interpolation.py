from utility import *


def gauss_forward_interpolation(x: list[float], y: list[float], xx: float) -> float:
    fd = construct_table(y)
    print_table(fd)

    start = find_start(x, xx)
    approx = fd[0][start]
    u = (xx - x[start]) / (x[1] - x[0])

    for i in range(1, max_it(start, len(y))):
        approx += fd[i][start] * calc_u(u, i) / fact(i)
        if i % 2 == 1:
            start -= 1

    return approx


def max_it(i: int, n: int) -> int:
    even_numbers = [i for i in range(2, n + 1, 2)]
    odd_numbers = [i for i in range(n if n % 2 == 1 else n - 1, 0, -2)]
    pattern = even_numbers + odd_numbers
    return pattern[i]


def calc_u(u: float, i: int) -> float:
    temp = u
    inc = 1
    for j in range(1, i):
        if j % 2 == 1:
            temp *= (u - inc)
        else:
            temp *= (u + inc)
            inc += 1
    return temp


if __name__ == '__main__':
    x = [21, 25, 29, 33, 37]
    y = [18.4708, 17.8144, 17.1070, 16.3432, 15.5154]
    value_to_find = 30

    print(f'Value at {value_to_find} is {gauss_forward_interpolation(x, y, value_to_find):.6f}')
