def fact(num):
    if num == 0:
        return 1

    result = num
    while num != 1:
        result *= num - 1
        num -= 1
    return result


def construct_table(y):
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
            print(f"{fdd[j][i]: <6.3f}", end=' ')
        print()
