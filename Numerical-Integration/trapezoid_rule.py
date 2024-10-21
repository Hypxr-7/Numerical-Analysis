a = 0
b = 0.8
n = 10

h = (b-a) / n

func = lambda x : 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

f = [func(a + i*h) for i in range(n+1)]

trap = h/2 * (f[0] + 2*sum(f[1:n]) + f[n])

print(f"{trap:.4f}")
