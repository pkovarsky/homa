"""
- Handle IOException, and other possible exceptions.
- Use Exception handling.
"""

# IOError
try:
    open("qweqr", 'r')
except IOError:
    print("File not found")


# Value Error
try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("It's not a number")
else:
    print("Entered value: ", x)


# Zero division
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Zero division")
finally:
    print("Idiot")
