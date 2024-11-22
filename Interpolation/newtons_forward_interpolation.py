from utility import *


def newtons_forward_interpolation(x: list[float], y: list[float], xx: float) -> float:
    n = len(x)
    fd = construct_table(y)
    print_table(fd)

    u = (xx - x[0]) / (x[1] - x[0])
    result = fd[0][0]

    for i in range(1, n):
        result += calc_u(u, i) * fd[i][0] / fact(i)

    return result


def calc_u(u: float, i: int) -> float:
    temp = u
    for j in range(1, i):
        temp *= (u - j)
    return temp


if __name__ == '__main__':
    x = [100, 150, 200, 250, 300, 350, 400]
    y = [10.63, 13.03, 15.04, 16.81, 18.42, 19.90, 21.27]
    value_to_find = 160

    print(f"Value at {value_to_find} is {newtons_forward_interpolation(x, y, value_to_find):.6f}")
