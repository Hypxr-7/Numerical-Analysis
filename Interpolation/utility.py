def fact(num: int) -> int:
    if num == 0:
        return 1

    result = num
    while num != 1:
        result *= num - 1
        num -= 1
    return result


def construct_table(y: list[float]) -> list[list[float]]:
    fd = [y]
    for i in range(1, len(y)):
        temp = []
        for j in range(0, len(y) - i):
            temp.append(fd[i - 1][j + 1] - fd[i - 1][j])
        fd.append(temp)
    return fd


def print_table(fdd: list[list]) -> None:
    for i in range(len(fdd)):
        for j in range(len(fdd[i])):
            print(f"{fdd[j][i]: <6.5f}", end=' ')
        print()


def find_start(x: list[float], xx: float) -> int:
    min = 99999
    min_index = 0
    for i in range(len(x)):
        if abs(x[i] - xx) < min:
            min = abs(x[i] - xx)
            min_index = i
    return min_index
