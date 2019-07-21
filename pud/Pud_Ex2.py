# N1 Implement to boolean function. Retrieve different type of object returns True or False
def boolvar(ob):
    return bool(ob)

boolvar(1)


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


# N 3Implement function to convert cm to inches and vice versa (convertCmToInches).
def convert_cm_to_inches(v, c=True):
    if c:
        return v / 2.54
    else:
        return v / 2.5


convert_cm_to_inches(5, False)


# 4 Implement printDiagonal function which wrap convertCmToInches function and print result.
# (call convertCmToInches and print result of evaluation)

def print_diagonal(v, c):
    return convert_cm_to_inches(v, c)


# 5 - Implement processArgs function which retrieves callback as a first argument, remaining args has various length.
# Default value for callback is a standard print function.
# Call this function with printDiagonal function and remaining args as cm or inches.
# processArgs(printDiagonal, 50, True)
# processArgs(print, 'test')
# processArgs(len, [])

def process_args(callback, *args, **kwargs):
    print(callback(*args, **kwargs))

process_args(print_diagonal, 50, True)
process_args(print, 'test')
process_args(len, [])
