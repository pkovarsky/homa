'ЗАДАНИЕ №3'

print('''ЗАДАНИЕ №3''')
print('\t')

A = (2, 26)
B = ['Petya', 'Artem']

print('Словарь, значением ключа которого является словарь')
print('\t')
ADRESSBOOK = {('Куйбышева', 5):{(A):(B)}}
print(ADRESSBOOK)

C = {"Lox", 4, 'Pidr', 7, 9, 10, "Pisos"}
D = {'Mosh', 'Sos', 10, 4, "Pisos"}

print('USE INTERSECTION')
print(C & D)
print('\t')

print('USE UNION')
print(C | D)
print('\t')

print('USE DIFFERENCE')
print(C - D, D - C)
print('\t')

print('USE UPDATE')
C.difference_update(A)
print(C)


print('Теперь должно быть норм.')
