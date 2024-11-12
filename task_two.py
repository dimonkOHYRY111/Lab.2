import math
from fibonacci_module import first_fibonacci

try:
    p = int(input("Введіть число p: "))
    fibonacci_num = first_fibonacci(p)
    print(f"Перше число Фібоначчі, більше за {p}: {fibonacci_num}")

except ValueError:
    print("Будь ласка, введіть коректне числове значення.")