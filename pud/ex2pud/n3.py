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
