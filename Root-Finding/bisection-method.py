import math

def main():
    bisection_method(f, 0, 1)


def f(x):
    return math.cos(x) - x * math.e ** x


def bisection_method(f, a, b, tol = 0.5, max_iterations = 100):
    if f(a) * f(b) >= 0:
        raise ValueError("The lower bound and upper bound must have different signs")
    
    print(f"{'Iteration':<10} {'Lower Bound':<15} {'Upper Bound':<15} {'Root':<15}")
    print("-" * 55)

    previous_c = 0
    for i in range(max_iterations):
        c = (b+a) / 2

        print(f"{i + 1:<10} {a:<15.6f} {b:<15.6f} {c:<15.6f}")
        
        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c) > 0:
            a = c
        
        if i != 0:
            if abs((previous_c - c) / previous_c)*100 <= tol:
                return
        
        previous_c = c

    print(f"Max iterations reached")

            
if __name__ == "__main__":
    main()

