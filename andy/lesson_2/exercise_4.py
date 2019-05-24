"""Implement printDiagonal function which wrap convertCmToInches function
and print result.(call convertCmToInches and print result of evaluation)"""


def convert_cm_to_inches(santimetr):
    """"convert cm to inches"""
    inch = santimetr * 0.3937007874
    return inch


def print_diagonal(length, width):
    """"Implement printDiagonal function"""
    length = convert_cm_to_inches(length)
    width = convert_cm_to_inches(width)
    diagonal = (length*length + width*width) ** 0.5
    print(diagonal)


print_diagonal(3, 4)
