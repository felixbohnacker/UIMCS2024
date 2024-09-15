# Function to compute GCD using the Euclidean algorithm
gcd <- function(a, b) {
  while(b != 0) {
    temp <- b
    b <- a %% b
    a <- temp
  }
  return(a)
}

# Example usage:
A <- 48
B <- 18
result <- gcd(A, B)
print(paste("GCD of", A, "and", B, "is", result))
