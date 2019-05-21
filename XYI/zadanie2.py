'ЗАДАНИЕ №2'

print('''ЗАДАНИЕ №2''')
print('\t')

print("Создаем длинный список")
YA = ['h', 'f', 'm', 'd', 'n', 'j', 'k', 'v', 'j', 'n', 'k', 'n', 'v', 'k',
      's', 'l', 'l', 'm', 'm']
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
