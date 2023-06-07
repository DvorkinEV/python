a = int(input())
b = int(input())
c = 3*((a+b)*(a+b)*(a+b)) +275*b*b - 127*a - 41
print(c)


a, b = int(input()), int(input())
print(3 * (a+b)**3 + 275 * b**2 - 127 * a - 41)


def func(a,b):
  return 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
print(func(int(input()),int(input())))



print((lambda a, b: 3*(a+b)**3+275*b*b-127*a-41)(int(input()), int(input())))

print((3 * ((a := int(input())) + (b := int(input()))) ** 3) + 275 * (b ** 2) - 127 * a - 41)

x = int(input())
y = int(input())


def func(a, b: int):
  const_1 = 275
  const_2 = 127
  const_3 = 41

  return 3 * (a + b) ** 3 + const_1 * b ** 2 - const_2 * a - const_3


print(func(x, y))