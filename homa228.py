print ('ax**2+bx+c=0')
a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c
if (d > 0):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 = ', x1)
    print('x2 = ', x2)
elif (d == 0):
    print('x = ', -b/(2*a))
else:
    print('Нет корней.')

print('zaebli, no spasibo')
print('zaebli, no spasibo')