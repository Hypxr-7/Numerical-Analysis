import math

def main():
    mullers_method(f, 2.5, 3, 3.5)


def f(x):
    return math.sin(x) / x


def mullers_method(f, x0, x1, x2, tol = 0.5, max_iterations = 100):
    print(f"{'Iteration':<10} {'x_n':<15} {'x_n+1':<15} {'x_n+2':<15} {'Root':<15}")
    print("-" * 55)


    for i in range(max_iterations):
        d0 = (f(x1) - f(x0)) / (x1 - x0)
        d1 = (f(x2) - f(x1)) / (x2 - x1)
        h0 = x1 - x0
        h1 = x2 - x1

        a = (d1 - d0) / (h1 + h0)
        b = a*h1 + d1
        c = f(x2)


        if (b > 0):
            x3 = x2 - (2*c) / (b + math.sqrt(b**2 - 4*a*c))
        else:
            x3 = x2 - (2*c) / (b - math.sqrt(b**2 - 4*a*c))
            

        print(f"{i + 1:<10} {x0:<15.6f} {x1:<15.6f} {x2:<15.6f} {x3:<15.6f}")
        
        
        if i != 0:
            if abs((x3 - x2) / x3)*100 <= tol:
                return
        
        x0, x1, x2 = x1, x2, x3
        

    print(f"Max iterations reached")

            
if __name__ == "__main__":
    main()

