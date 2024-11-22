def lagrange_interpolation(x: list[float], y: list[float], xx: float) -> float:
    approx = 0
    for i in range(len(y)):
        product = y[i]
        for j in range(len(y)):
            if i != j:
                product *= ((xx - x[j]) / (x[i] - x[j]))
        approx += product
    return approx


if __name__ == "__main__":
    x = [-1, 0, 3, 6, 7]
    y = [3, -6, 39, 822, 1611]
    value_to_find = 4

    print(f"Value at {value_to_find} is {lagrange_interpolation(x, y, value_to_find):.6f}")
