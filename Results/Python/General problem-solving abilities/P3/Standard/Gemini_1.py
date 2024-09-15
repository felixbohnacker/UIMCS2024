def count_divisors_divisible_by_3(N):
  """Counts the number of divisors of N that are divisible by 3.

  Args:
    N: The integer for which to count the divisors.

  Returns:
    The number of divisors of N that are divisible by 3.
  """

  count = 0
  for i in range(3, N + 1, 3):  # Iterate over multiples of 3 from 3 to N
    if N % i == 0:  # Check if i is a divisor of N
      count += 1
  return count

# Example usage:
N = 24
result = count_divisors_divisible_by_3(N)
print("Number of divisors of", N, "divisible by 3:", result)