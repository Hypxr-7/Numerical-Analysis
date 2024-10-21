def main():
    qd_algorithm()


def get_coefficients():
    return {
        0: 1,
        1: -32,
        2: 160,
        3: -256,
        4: 128,
    }


def print_q(q, k):
    print(f"{'':<10}", end="")
    for value in q[k]:
        print(f"{value:<20.3f}", end="")
    print()


def print_e(e, k):
    for value in e[k]:
        print(f"{value:<20.3f}", end="")
    print()


def qd_algorithm(iterations=10):
    q = []
    e = []
    coefficients = get_coefficients()
    n = len(coefficients) - 1

    for i in range(n):
        print(f"{'e'+str(i):<10} {'q'+str(i):<10}", end="")
    print(f"{'e'+str(n):<10}")

    temp_q = []
    temp_e = []
    for i in range(n):
        if i == 0:
            temp_q.append(-coefficients[n-1] / coefficients[n])
            temp_e.append(0)
        else:
            temp_q.append(0)
            temp_e.append(coefficients[n-i-1] / coefficients[n-i])
    temp_e.append(0)

    q.append(temp_q[:])
    e.append(temp_e[:])

    for i in range(iterations):
        temp_q = [0] * n
        temp_e = [0] * (n + 1)

        for j in range(n):
            temp_q[j] = e[i][j+1] - e[i][j] + q[i][j]
        q.append(temp_q[:])

        for j in range(1, n):
            temp_e[j] = q[i+1][j] / q[i+1][j-1] * e[i][j]
        temp_e[0] = 0
        temp_e[n] = 0

        e.append(temp_e[:])

        print_q(q, i)
        print_e(e, i)


if __name__ == "__main__":
    main()
