"""Implement function to convert
cm to inches and vice versa (convertCmToInches)."""


def convert_to_cm_or_inches(value, measurement):
    """"convert cm to inches"""
    if measurement == "cm":
        result = value * 0.3937007874
    elif measurement == "inches":
        result = value * 2.54
    else:
        result = "Invalid measurement"
    return result


print(convert_to_cm_or_inches(20, "cm"))
print(convert_to_cm_or_inches(7.874015748, "inches"))
print(convert_to_cm_or_inches(29, "Igor dick is big"))
