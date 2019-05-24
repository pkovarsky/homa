"""Implement 2 functions for calculation Factorial number
(Method retrieves number, returns it Factorial).
  First function uses while loop for calculation
  Second function uses for loop for calculation
  For avoid stack overflow do not calculate Factorial number more than 100500.
  Use default function argument for limit.
  Negative, fractional, not a number argument forbidden."""


def get_factorial_while(number):
    """""First function uses while loop for calculation"""
    factorial = 1
    i = 1
    while i <= number:
        if factorial < 100500:
            factorial = factorial * i
            i += 1
        else:
            return False
    return factorial


def get_factorial_for(number):
    """""Second function uses for loop for calculation"""
    factorial = 1
    for i in range(1, number+1):
        if factorial < 100500:
            factorial = factorial * i
            i += 1
        else:
            return False
    return factorial


print(get_factorial_while(4))
print(get_factorial_for(4))
