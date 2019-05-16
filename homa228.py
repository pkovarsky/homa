PETYA = ('ak', 'gh', 'gs', 'gi', 'gg', 'og', 'hs', 'aa', 'se', 'gf', 'jv', 'av', 'sv', 'gz', 'sf', 'ca', 'iv', 'zc',
         'gd', 'fh', 'ai', 'fa', 'hg', 'ga', 'lx', 'ar', 'gv', 'sa', 'gw', 'sv', 'fp', 'sr', 'fp', 'og', 'pg', 're')

print('Список из 20 переменных от 5ой с конца')
print(PETYA[-5:-25:-1])

print('Превратили этот список в словарь А')
PETYA = dict(PETYA)
print(PETYA)

print('Отсортировали ключи словаря А')
sorted(PETYA)
print(PETYA.keys())

print('Никогда не думал, что я настолько тупой')
print('\t')

print('''ЗАДАНИЕ №2''')
print('\t')

print("Создаем длинный список")
YA = ['h', 'f', 'm', 'd', 'n', 'j', 'k', 'v', 'j', 'n', 'k', 'n', 'v', 'k', 's', 'l', 'l', 'm', 'm']
print(YA)

print("Расширяем список другим списком")
YA.extend(['h', 'f', 'm', 'd', 'n', 'j', 'k', 'v', 'j', 'n'])
print(YA)

print("Убираем повторяющееся значения")
YA = list(dict.fromkeys(YA))
print(YA)

print("Удаляем средний символ из строки, используя слайс")
TI = len(YA)//2
del YA[TI:TI+1]
print(YA)

print('\t')


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
