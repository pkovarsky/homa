def pizduk(n):
    if type(n) == int and n >= 0:
        pass
    else:
        return 'ПОШОЛ НА ХОЙ 2'
    if n < 100500:
        pass
    else:
        return 'ПОШОЛ НА ХОЙ'
    X = 1

    for i in range(2, n + 1):
        X = X * i
    return X

print(pizduk(-3))
print(pizduk(0))

