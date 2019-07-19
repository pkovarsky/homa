#N1

istrue = 1 + 1 and 4 / 2 and True
if istrue is True:
    pass
else:
    print("sucker")

isfalse = {} or [] or ""
if isfalse is True:
    print("13")
else:
    print('zl9dinaN1')

#N2

def factwhile(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return print(n*f)
factwhile(6) #vyzov

def factfor(n):
    f = 1
    for i in range (2, n+1):
        f *= i
    return print(f)
factfor(6)

#N3,4
def convertcmtoinches(v):
    #def printDiagonal(v):
        #return convertcmtoinches(v)
    v = (float(input('Enter value here:')))
    c = (str(input("To cm or to inches:")))
    if c == 'cm':
        return print(v / 2.54)
    elif c == "i":
        return print(v * 2.54)
    else:
        return print("Whoopsblyad")


#5
