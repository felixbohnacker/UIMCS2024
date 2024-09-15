def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
A = 48
B = 18
print("GCD of", A, "and", B, "is", gcd(A, B))
