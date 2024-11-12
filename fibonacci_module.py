def first_fibonacci(p):
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b

    return b