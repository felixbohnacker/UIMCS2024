def count_divisors_divisible_by_3(N):
    count = 0
    # Loop through all potential divisors
    for i in range(1, N + 1):
        if N % i == 0:  # Check if i is a divisor of N
            if i % 3 == 0:  # Check if the divisor is divisible by 3
                count += 1
    return count

# Example usage
N = 12
result = count_divisors_divisible_by_3(N)
print(f"The number of divisors of {N} that are divisible by 3 is: {result}")
