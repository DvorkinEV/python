n = int(input())
a = n//100
b = n//10%10
c = n%10
d = a+b+c
e = a*b*c
print("Сумма цифр =", d)
print("Произведение цифр =", e)


a = str(input())
print('Сумма цифр =', int(a[0]) + int(a[1]) + int(a[2]))
print('Произведение цифр =', int(a[0]) * int(a[1]) * int(a[2]))


[print(f'Сумма цифр = {a+b+c}\nПроизведение цифр = {a*b*c}') for a,b,c in [[int(i) for i in input()]]]


a = input()
sum_ai = 0
mul_ai = 1
for i in range(len(a)):
    sum_ai += int(a[i])
    mul_ai *= int(a[i])
print('Сумма цифр =', sum_ai)
print('Произведение цифр =', mul_ai)


def digits_list(number):
    return [(number % (10**n)) // (10**(n-1)) for n in range(len(str(number)), 0, -1)]

digits = digits_list(int(input()))
prod = 1
for d in digits:
    prod = prod * d
print(f"Сумма цифр = {sum(digits)}\nПроизведение цифр = {prod}")


num = int(input())
summ = 0
mult = 1
while(num > 0):
	summ += num % 10
	mult *= num % 10
	num //= 10

print(f"Сумма цифр = {summ}")
print(f"Произведение цифр = {mult}")



class ThreeDigitNumber():
    def __init__(self, number):
        self.number = number
        self.hundreds = self.number // 100
        self.tens = self.number // 10 % 10
        self.units = self.number % 10
    def sum_digit(self):
        return self.hundreds + self.tens + self.units
    def mul_digit(self):
        return self.hundreds * self.tens * self.units
    def display_something(self):
        print(f"Сумма цифр = {self.sum_digit()}")
        print(f"Произведение цифр = {self.mul_digit()}")

ThreeDigitNumber(int(input())).display_something()



abc = int(input())
a, b, c = abc // 100, (abc % 100) // 10 , abc % 10
print(f'Сумма цифр = {a + b + c}', f'Произведение цифр = {a * b * c}', sep='\n')



a = int(input())
s = 0
p = 1
while a > 0:
    s+= a % 10
    p *= a % 10
    a//=10
print('Сумма цифр =', s)
print('Произведение цифр =', p)


print((lambda x: f'Сумма цифр = {sum(x)}\nПроизведение цифр = {x[0] * x[1] * x[2]}')([int(_) for _ in input().strip()]))


print((lambda x: f' Сумма цифр = {x//100+((x-x//100*100)//10)+(x-x//100*100-((x-x//100*100)//10)*10)}\nПроизведение цифр = {x//100*((x-x//100*100)//10)*(x-x//100*100-((x-x//100*100)//10)*10)}')(int(input())))


a = list(input())
sm = 0
pr = 1
for j in a:
    sm += int(j)
    pr *= int(j)
print(f'Сумма цифр = {sm}', f'Произведение цифр = {pr}', sep='\n')


[print(f'Сумма цифр = {a // 100 + a % 10 + (a % 100) // 10}', f'Произведение цифр = {(a // 100) * (a % 10) * ((a % 100) // 10)}', sep='\n') for a in [int(input())] ]


from functools import reduce

number = []
for i in range(1):
    number.append(int(input()))

values = []

while number[0] > 0:
    digit = number[0] % 10
    values.append(digit)
    number[0] = number[0] // 10

print(f'Сумма цифр = {sum(values)}\nПроизведение цифр =', reduce(lambda x, y: x * y, values))


def pr(x):
    p = 1
    x = str(x)
    for y in x:
        p *= int(y)
    return(p)


def suma(x):
    s = 0
    x = str(x)
    for y in x:
        s += int(y)
    return(s)

x = int(input())
print("Сумма цифр =", suma(x))
print('Произведение цифр =', pr(x))


number = [int(c) for c in input()]
total = 1
for i in range(len(number)):
    total = total * number[i]
print(f'Сумма цифр = {sum(number)}', f'Произведение цифр = {total}', sep='\n')




a = [int(i) for i in input()]
print(f'Сумма цифр = {a[0]+a[1]+a[2]}\nПроизведение цифр = {a[0]*a[1]*a[2]}')



def addArr(a ):

    arr = []
    for i in list(a):
        arr.append( int(i) )
    return arr

def calc(caclEl):

    print(f'Сумма цифр = {sum(caclEl)}')

    acc = 1
    for i in caclEl:
        acc = acc*i
    print(f'Произведение цифр = {acc}')

a = input()
caclEl = addArr(a)

calc(caclEl)

x = int(input())
s = 0
p = 1
while x:
    d = x%10
    s = s + d
    p = p * d
    x //= 10
print('Сумма цифр', '=', s)
print('Произведение цифр', '=', p)



num = int(input())
if num > 99 and num < 1000:
    a = num % 10
    b = (num % 100) // 10
    c = num // 100
    print('Сумма цифр =', a + b + c)
    print('Произведение цифр =', a * b * c)
else:
    print('Число должно быть от 100 до 999')

s = 0
p = 1
for i in input():
    s += int(i)
    p *= int(i)
print(f'Сумма цифр = {s}')
print(f'Произведение цифр = {p}')

[print(f'Сумма цифр = {a + b + c}\nПроизведение цифр = {a * b * c}') for a, b, c, in [[int(i) for i in input()]]]
#списочное выражение


a, b, c = input()

print('Сумма цифр =', int(a) + int(b) + int(c))
print('Произведение цифр =', int(a) * int(b) * int(c))


def number():
    num = int(input())
    first, second, third = num // 100, (num // 10) % 10, (num % 100) % 10
    return print(f"Сумма цифр = {first + second + third}",
                 f"Произведение цифр = {first * second * third}", sep='\n')


number()

from functools import reduce
from operator import mul

lst = [int(i) for i in input()]

lst_mul = reduce(mul, lst)

print(f'Сумма цифр = {sum(lst)}\nПроизведение цифр = {lst_mul}')


n = int (input ())


def sj(n):
    n1 = n // 100
    n2 = (n % 100) // 10
    n3 = n % 10
    sm = n1 + n2 + n3
    return sm


def sj1(n):
    n1 = n // 100
    n2 = (n % 100) // 10
    n3 = n % 10
    su = n1 * n2 * n3
    return su


print ('Сумма цифр =', sj (n))
print ('Произведение цифр =', sj1 (n))


n = int(input())

s, t = 0, 1

while n:
    num = n % 10
    s += num
    t *= num
    n //= 10

print(f"""Сумма цифр = {s}
Произведение цифр = {t}""")

from functools import reduce
n=[int(i) for i in input()]
print(f"Сумма цифр = {sum(n)}", f"Произведение цифр = {reduce(lambda x,y: x*y, n)}", sep="\n")

#Я так и знал, что должна же быть команда, которая может разбить число по разрядам на отдельные числа


a,b,c=map(int, input())
print(f"Сумма цифр = {a+b+c}\nПроизведение цифр = {a*b*c}")

a = int(input())
b=0
c=1
while (a>0):
    b += a%10
    c *= a%10
    a //= 10

print("Сумма цифр =", b)
print("Произведение цифр =", c)



