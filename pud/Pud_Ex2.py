#N1 Implement to boolean function. Retrieve different type of object returns True or False
def boolvar(ob):
    return bool(ob)
boolvar(0)


#N2  Implement 2 functions for calculation Factorial number (Method retrieves number, returns it Factorial).
#First function uses while loop for calculation
#Second function uses for loop for calculation
#For avoid stack overflow do not calculate Factorial number more than 100500. Use default function argument for limit.
#Negative, fractional, not a number argument forbidden.

def factwhile(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return print(n*f)
factwhile(1) #vyzov 720

def factfor(n):
    f = 1
    for i in range (2, n+1):
        f *= i
    return print(f)
factfor(1) #39916800

#N 3Implement function to convert cm to inches and vice versa (convertCmToInches).
def convertcmtoinches():
    v = (float(input('Enter value here:')))
    c = (str(input("To cm or to inches:")))
    if c == 'cm':
        return print(v / 2.54)
    elif c == "i":
        return print(v * 2.54)
    else:
        return print("Whoopsblyad")
convertcmtoinches()


#4 Implement printDiagonal function which wrap convertCmToInches function and print result.
#(call convertCmToInches and print result of evaluation).
#5 - Implement processArgs function which retrieves callback as a first argument, remaining args has various length.
#Default value for callback is a standard print function.
#Call this function with printDiagonal function and remaining args as cm or inches.
#processArgs(printDiagonal, 50, True)
#processArgs(print, 'test')
#processArgs(len, [])