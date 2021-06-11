summ = 0


def fractal(x):
    for i in range(x):
        i *= i
        summ += summ
