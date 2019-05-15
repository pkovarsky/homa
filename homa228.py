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
