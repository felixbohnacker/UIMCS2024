def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

# Example usage:
A = int(input("Enter the first number (A): "))
B = int(input("Enter the second number (B): "))

result = gcd(A, B)
print(f"The GCD of {A} and {B} is: {result}")
