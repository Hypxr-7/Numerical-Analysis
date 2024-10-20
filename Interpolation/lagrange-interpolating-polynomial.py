def interpolate(dp, n, x):
    sum = 0
    for i in range(n):
        product = dp['f'][i]
        for j in range(n):
            if i != j: 
                product = product * ((x - dp['x'][j]) / (dp['x'][i] - dp['x'][j]))
        sum += product

    print(f"{sum:.6f}")


if __name__ == "__main__":
    data = {
        'x': [1,   3,    5,    7,    13], 
        'f': [800, 2310, 3090, 3940, 4755],
    }
    interpolate(data, len(data['x']), 10)
