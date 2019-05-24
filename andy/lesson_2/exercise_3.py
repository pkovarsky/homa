"""Implement function to convert
cm to inches and vice versa (convertCmToInches)."""


def convert_cm_to_inches(santimetr):
    """"convert cm to inches"""
    inch = santimetr * 0.3937007874
    return inch


def convert_inches_to_cm(inches):
    """"convert inches to cm"""
    santimetr = inches * 2.54
    return santimetr


print(convert_cm_to_inches(20))
print(convert_inches_to_cm(7.874015748))
