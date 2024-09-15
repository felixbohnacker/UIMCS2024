def count_divisors_divisible_by_3(N):
    count = 0
    # Iterate through possible divisors from 1 to sqrt(N)
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:  # i is a divisor of N
            if i % 3 == 0:  # Check if i is divisible by 3
                count += 1
            # Check the corresponding divisor N // i
            if i != N // i and (N // i) % 3 == 0:
                count += 1
    return count

# Example usage:
N = 36
result = count_divisors_divisible_by_3(N)
print(f"The number of divisors of {N} that are divisible by 3 is: {result}")
