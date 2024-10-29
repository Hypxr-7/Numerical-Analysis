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

def construct_table(y):
    fd = [y]
    for i in range(1, len(y)):
        temp = []
        for j in range(0, len(y)-i):
            temp.append(fd[i-1][j+1] - fd[i-1][j])
        fd.append(temp)
    return fd