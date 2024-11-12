import math

def calculate_z(x):
    if x > 45:
        return -math.sqrt(x)
    else:
        return math.sin(2 * x)


def first_fibonacci(p):
    a, b = 1, 1
    while b <= p:
        a, b = b, a + b

    return b

try:
    x = int(input("Введіть значення x: "))
    z = calculate_z(x)
    print(f"Значення z: {z}")

    p = int(input("Введіть число p: "))
    fibonacci_num = first_fibonacci(p)
    print(f"Перше число Фібоначчі, більше за {p}: {fibonacci_num}")

except ValueError:
    print("Будь ласка, введіть коректне числове значення.")