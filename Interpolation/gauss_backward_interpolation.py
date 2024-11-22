from utility import *


def gauss_backward_interpolation(x: list[float], y: list[float], xx: float) -> float:
    fd = construct_table(y)
    print_table(fd)

    start = find_start(x, xx)
    approx = fd[0][start]
    u = (xx - x[start]) / (x[1] - x[0])

    start -= 1
    for i in range(1, max_it(start + 1, len(fd))):
        approx += fd[i][start] * calc_u(u, i) / fact(i)
        if i % 2 == 0:
            start -= 1

    return approx


def max_it(i: int, n: int) -> int:
    odd_numbers = [i for i in range(1, n + 1, 2)]
    even_numbers = [i for i in range(n if n % 2 == 0 else n - 1, 1, -1)]
    pattern = odd_numbers + even_numbers
    return pattern[i]


def calc_u(u: float, i: int) -> float:
    temp = u
    inc = 1
    for j in range(1, i):
        if j % 2 == 0:
            temp *= (u - inc)
            inc += 1
        else:
            temp *= (u + inc)
    return temp


if __name__ == '__main__':
    x = [39, 49, 59, 69, 79, 89]
    y = [12, 15, 20, 27, 39, 52]
    value_to_find = 62

    print(f'Value at {value_to_find} is {gauss_backward_interpolation(x, y, value_to_find):.6f}')
