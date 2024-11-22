from utility import *


def newtons_divided_difference(x: list[float], y: list[float], xx: int) -> float:
    fdd = get_fdd_table(x, y)
    print("Divided Difference Table:")
    print_table(fdd)

    approx = fdd[0][0]
    product = xx - x[0]

    for i in range(1, len(fdd)):
        approx += fdd[i][0] * product
        product *= (xx - x[i])

    return approx


def get_fdd_table(x: list[float], y: list[float]) -> list[list[float]]:
    fdd = [y]
    for i in range(1, len(y)):
        temp = []
        for j in range(0, len(y) - i):
            temp.append((fdd[i - 1][j + 1] - fdd[i - 1][j]) / (x[j + i] - x[j]))
        fdd.append(temp)
    return fdd


if __name__ == '__main__':
    x = [3, 7, 9, 10]
    y = [168, 120, 72, 63]
    value_to_find = 6

    print(f"Value at {value_to_find} is {newtons_divided_difference(x, y, value_to_find):.6f}")
