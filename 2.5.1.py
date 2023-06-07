b1 = int(input())
q = int(input())
n = int(input())
b = b1 * q**(n - 1)
print(b)


[print(b*q**(n-1)) for b,q,n in [[int(input()) for _ in 'bqn']]]


(lambda b,q,n:print(b*q**(n-1)))(*[int(input())for _ in range(3)])


b1, q, n = int(input()), int(input()), int(input())
print(f'{b1 * q ** (n-1)}')


def geo_prog(a, b, c):
    return a * b ** (c - 1)
print(geo_prog(int(input()), int(input()), int(input())))


print((lambda b_1, q, n: b_1 * q ** (n - 1))(int(input()), int(input()), int(input())))


def progression(b_1, q, n):
    prog = b_1 * q ** (n -1)
    return prog
b_1, q, n = int(input()), int(input()), int(input())
print(progression(b_1, q, n))




# put your python code here
''' Geometric progression '''

def a_member_of_the_geometric_progression(b1, q, n):  # функция для для нахождения n-ого члена геометрической прогрессии
    x = b1 * q ** (n - 1)
    return x

b1 = int(input())  # ввод с клавиатуры число (целое)
q = int(input())  # ввод с клавиатуры число (целое)
n = int(input())  # ввод с клавиатуры число (целое)

print(a_member_of_the_geometric_progression(b1, q, n))  # вывод n-ого члена геометрической прогрессии
