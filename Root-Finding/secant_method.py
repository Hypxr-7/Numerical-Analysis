import math

def main():
    newton_raphson_method(f, 0, 1)


def f(x):
    return math.cos(x) - x * math.e ** x


def newton_raphson_method(f, x0, x1, tol = 0.5, max_iterations = 100):
    print(f"{'Iteration':<10} {'x_n':<15} {'x_n+1':<15} {'Root':<15}")
    print("-" * 55)

    previous_c = 0
    for i in range(max_iterations):
        c = x1 - (x0 - x1)*f(x1) / (f(x0) - f(x1))

        print(f"{i + 1:<10} {x0:<15.6f} {x1:<15.6f} {c:<15.6f}")
        
        x0 = x1
        x1 = c
        
        if i != 0:
            if abs((previous_c - c) / previous_c)*100 <= tol:
                return
        
        previous_c = c

    print(f"Max iterations reached")

            
if __name__ == "__main__":
    main()

