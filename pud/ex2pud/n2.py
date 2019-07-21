# N2  Implement 2 functions for calculation Factorial number (Method retrieves number, returns it Factorial).
# First function uses while loop for calculation
# Second function uses for loop for calculation
# For avoid stack overflow do not calculate Factorial number more than 100500. Use default function argument for limit.
# Negative, fractional, not a number argument forbidden.

def factwhile(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    while n > 1 or n is 0:
        f *= n
        n -= 1
    return n * f


print(factwhile(0))  #
print(factwhile(1))  #
print(factwhile(2))  #
print(factwhile(6))  #


def fact_for(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return print(f)


fact_for(6)  #