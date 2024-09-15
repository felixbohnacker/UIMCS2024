def fibonacci_series(n):
  """Calculates the Fibonacci series up to the given number n.

  Args:
    n: A positive integer.

  Returns:
    A list containing the Fibonacci series up to n.
  """

  fib_series = [0, 1]
  while fib_series[-1] <= n:
    fib_series.append(fib_series[-1] + fib_series[-2])
  return fib_series

# Get the input from the user
n = int(input("Enter a positive integer: "))

# Calculate the Fibonacci series
result = fibonacci_series(n)

# Print the result
print("Fibonacci series up to", n, ":")
print(result)