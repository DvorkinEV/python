a = int(input())
V = a*a*a
S = 6*a*a
print("Объём =", V)
print("Площадь полной поверхности =", S)

a = int(input())
print('Объем =', a**3)
print('Площадь полной поверхности =', 6*(a**2))


a = int(input())
print(f'Объем = {a**3}\nПлощадь полной поверхности = {6*a**2}')

# Чтобы не нагромождать print, использовал f-строку.
# Тупо в print перед кавычкой нужно написать f.
# f-строки поддерживают арифметические действия, поэтому
# внутри { } можно написать имя переменной и произвести действия.
# да даже можно имя и не писать, а просто что-то сложить


[print('Объем = ', i**3, '\n', 'Площадь полной поверхности = ', 6*i**2, sep='') for i in [int(input())]]


exec("print(f'Объем = {a ** 3}\\nПлощадь полной поверхности = {6 * a ** 2}')", {'a': int(input())})