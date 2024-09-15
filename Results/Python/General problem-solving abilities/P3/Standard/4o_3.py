def count_divisors_divisible_by_3(N):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0 and i % 3 == 0:
            count += 1
    return count

# Example usage:
N = 18
result = count_divisors_divisible_by_3(N)
print(f"The number of divisors of {N} that are divisible by 3 is: {result}")
