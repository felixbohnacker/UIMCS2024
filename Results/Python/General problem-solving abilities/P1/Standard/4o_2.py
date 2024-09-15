def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))

result = gcd(A, B)
print(f"The GCD of {A} and {B} is: {result}")
