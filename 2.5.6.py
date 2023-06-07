min = int(input())
print(min, "мин - это", min//60, "час", min%60, "минут.")

minutes = int(input())
print(f'{minutes} мин - это {minutes // 60} час {minutes % 60} минут.')

print((lambda x: f'{x} мин - это {x // 60} час {x % 60} минут.')(int(input())))


n = int(input())
print('{time} мин - это {chas} час {min} минут.'.format(time = n, chas = n // 60, min = n - (n//60 * 60)))


aa = int(input())
a = aa // 60
m = aa % 60
if a == 1 or a == 21:
    b = 'час'
elif a % 10 < 5 and a not in [0, 10, 11, 12, 13, 14, 20]:
    b = 'часа'
else:
    b = 'часов'
if m % 10 == 1 and m != 11:
    mm = 'минута'
elif m % 10 < 5 and m not in [11, 12, 13, 14,] and m % 10 != 0:
    mm = 'минуты'
else:
    mm = 'минут'
print(f'{aa} мин - это {a} {b} {m} {mm}.')