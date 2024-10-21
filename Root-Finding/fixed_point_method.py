import math

def main():
    fixed_point_method(g, 0.5)

def f(x):
    return math.sin(math.sqrt(x)) - x

def g(x):
    return math.sin(math.sqrt(x))

def fixed_point_method(g, x, tol = 0.01, max_iterations = 100):
    print(f"{'Iteration':<10} {'x_n':<15} {'x_n+1':<15}")
    print("-" * 55)

    for i in range(max_iterations):
        x_n = g(x)

        print(f"{i + 1:<10} {x:<15.6f} {x_n:<15.6f}")
        
        
        if i != 0:
            if abs((x - x_n) / x)*100 <= tol:
                return
            
        x = x_n

    print(f"Max iterations reached")

            
if __name__ == "__main__":
    main()

