import math

def main():
    newton_raphson_method(f, f_der, 0)


def f(x):
    return math.cos(x) - x * math.e ** x

def f_der(x):
    return -math.sin(x) -(x * math.e ** x + math.e ** x)


def newton_raphson_method(f, f_der, a, tol = 0.5, max_iterations = 100):
    print(f"{'Iteration':<10} {'Start Value':<15} {'Root':<15}")
    print("-" * 55)

    previous_c = 0
    for i in range(max_iterations):
        c = a - f(a) / f_der(a)

        print(f"{i + 1:<10} {a:<15.6f} {c:<15.6f}")
        
        a = c
        
        if i != 0:
            if abs((previous_c - c) / previous_c)*100 <= tol:
                return
        
        previous_c = c

    print(f"Max iterations reached")

            
if __name__ == "__main__":
    main()

