def conventional_exponentiation(a: int, b: int) -> int:
    result = 1
    for _ in range(b):
        result *= a
    return result
def divide_and_conquer_exponentiation(a: int, b: int) -> int:
    if b == 0:
        return 1
    elif b % 2 == 0:  
        half = divide_and_conquer_exponentiation(a, b // 2)
        return half * half
    else:  
        return a * divide_and_conquer_exponentiation(a, b - 1)
base = 2
exponent = 10
print(f"Conventional Approach: {base}^{exponent} = {conventional_exponentiation(base, exponent)}")

print(f"Divide & Conquer Approach: {base}^{exponent} = {divide_and_conquer_exponentiation(base, exponent)}")
