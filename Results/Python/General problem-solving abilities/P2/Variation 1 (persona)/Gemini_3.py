def fibonacci_series(N):
  """Calculates the Fibonacci series up to N, including N if it's part of the series.

  Args:
    N: A positive integer.

  Returns:
    A list containing the Fibonacci series up to N.
  """

  if N <= 0:
    return []

  fib_series = [0, 1]
  while fib_series[-1] < N:
    next_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(next_fib)

  # If N is not in the series, remove the last element
  if fib_series[-1] > N:
    fib_series.pop()

  return fib_series

# Example usage:
N = 13
result = fibonacci_series(N)
print(result)