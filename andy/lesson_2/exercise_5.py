"""Implement processArgs function which retrieves callback as a first argument,
  remaining args has various length.
  Default value for callback is a standard print function.
  Call this function with printDiagonal function
  and remaining args as cm or inches.
  processArgs(printDiagonal, 50, True)
  processArgs(print, 'test')
  processArgs(len, [])"""


def process_args(*args):
    """Implement processArgs function"""
    for value in args:
        print(value)


def convert_cm_to_inches(santimetr):
    """"convert cm to inches"""
    inch = santimetr * 0.3937007874
    return inch


def print_diagonal(length, width):
    """"Implement printDiagonal function"""
    length = convert_cm_to_inches(length)
    width = convert_cm_to_inches(width)
    diagonal = (length*length + width*width) ** 0.5
    return diagonal


process_args([print_diagonal(3, 4), 50, True])
PRINT = {"Nizhnik", "Pidor"}
process_args(PRINT, 'test')
process_args(len(PRINT), [])
