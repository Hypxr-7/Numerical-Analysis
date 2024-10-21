def simp13(h, f0, f1, f2):
    return 2*h*(f0 + 4*f1 + f2) / 6


def simp13m(h, n, f):
    sum_simp = f[0]
    for i in range(1, len(f)-1, 2):
        sum_simp += 4 * f[i] + 2 * f[i + 1]
    sum_simp += 4*f[n-2] + f[n-1]
    return h * sum_simp / 3


def simp38(h, f0, f1, f2, f3):
    return 3*h * (f0 + 3*(f1+f2) + f3) / 8


def simp_interpolate(a, b, n, f):
    sum_simp = 0
    h = (b-a) / n
    if n == 1:
        print("Only one interval, use trapezoid rule")
        return
    else:
        m = n
        odd = n / 2 - n // 2
        if odd > 0 and n > 1:
            sum_simp = simp38(h, f[n-3], f[n-2], f[n-1], f[n])
            f = f[:-3]
            m = n - 3
        if m > 1:
            if len(f) == 3:
                sum_simp += simp13(h, f[0], f[1], f[2])
            else:
                sum_simp += simp13m(h, n, f)
        return sum_simp

if __name__ == '__main__':
    func = [0.2, 1.296919, 1.743393, 3.186015, 3.181929, 0.232]
    print(simp_interpolate(0, 0.8, 5, func))
