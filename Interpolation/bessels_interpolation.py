from math import factorial
from utility import *
from gauss_forward_interpolation import calc_u as forward_u
from gauss_backward_interpolation import calc_u as backward_u


def bessels_interpolation(x: list[float], y: list[float], xx: float) -> float:
    fd = construct_table(y)
    print_table(fd)

    start = find_start(x, xx)
    approx = (fd[0][start] + fd[0][start + 1]) / 2
    u = (xx - x[start]) / (x[1] - x[0])

    for i in range(1, max_it(start, len(x))):
        if i % 2 == 1:
            approx += fd[i][start] * calc_u(u, i) / factorial(i)
        else:
            approx += ((fd[i][start] + fd[i][start - 1]) / 2) * calc_u(u, i) / factorial(i)
            start -= 1

    return approx


def max_it(i: int, n: int) -> int:
    if n % 2 == 0:
        even_sequence = list(range(2, n + 1, 2))
        pattern = even_sequence + even_sequence[-2::-1] + [0]
    else:
        even_sequence = list(range(2, n, 2))
        pattern = even_sequence + even_sequence[::-1] + [0]
    return pattern[i]


def calc_u(u: float, i: int) -> float:
    return (forward_u(u, i) + backward_u(u-1, i)) / 2


if __name__ == '__main__':
    x = [10, 11, 12, 13, 14]
    y = [20.9848, 22.9816, 24.9781, 26.9743, 28.9702]
    value_to_find = 11.5

    print(f"Value at {value_to_find} is {bessels_interpolation(x, y, value_to_find)}")
